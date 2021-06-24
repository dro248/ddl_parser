from simple_ddl_parser import DDLParser
from collections import deque


class DDL2AlembicParser:
    """
    The DDL2AlembicParser class converts DDL to Alembic.
    """

    @staticmethod
    def get_index(string, idx):
        """
        Given a string and the index of an open parenthesis,
        return the index of its closing parenthesis.
        """
        # If input is invalid.
        if string[idx] != "(":
            return -1

        # Create a deque to use it as a stack.
        my_deque = deque()

        # Traverse through all elements starting from idx.
        for item in range(idx, len(string)):

            # Pop a starting paren for every closing paren
            if string[item] == ")":
                my_deque.popleft()

            # Push all starting parens
            elif string[item] == "(":
                my_deque.append(string[idx])

            # If deque becomes empty
            if not my_deque:
                return item

        return -1

    @classmethod
    def clean_ddl(cls, raw_ddl: str):
        """Prepares the DDL so that it is ready to be parsed."""
        # remove backticks
        ddl = raw_ddl.replace("`", "")

        # remove stuff at the end of ddl that doesn't play well with the parser
        ddl_end_index = cls.get_index(ddl, ddl.find("(")) + 1
        clean_ddl = ddl[:ddl_end_index]
        return f"{clean_ddl};"

    @staticmethod
    def format_column(column_dict: dict) -> str:
        """Takes a column_dict and formats it into a properly formatted SQLAlchemy Column."""
        
        column_name = column_dict.get("name")
        
        # Sqlalchemy (sa) or Snowflake (sf)
        orm_type = 'sa'
        
        ##################################################
        #            SPECIAL COLUMN MAPPINGS             #
        ##################################################
        
        # Fix TIMESTAMP to be TIMESTAMP_TZ()
        if column_dict.get("type").upper() == "TIMESTAMP":
            column_type = "TIMESTAMP_TZ"
            orm_type = 'sf'
            
        elif column_dict.get("type").upper() == "DATE":
            column_type = "DATE"
            orm_type = "sf"
        
        else:
            column_type = column_dict.get("type").upper()

        # Format `column_size`
        # no args -> '()'
        if not column_dict.get("size"):
            column_size = "()"

        # one NUMBER arg -> '(123)'
        elif isinstance(column_dict.get("size"), int):
            column_size = f"({column_dict.get('size')})"

        # multiple args -> '(1, 3)'
        elif isinstance(column_dict.get("size"), tuple):
            column_size = str(column_dict.get("size"))

        else:
            raise ValueError(
                f"column_size: I don't know how to parse '{column_dict.get('size')}' (type: {type(column_dict.get('size'))})"
            )

        output = f"sa.Column('{column_name}', {orm_type}.{column_type}{column_size})"
        return output

    @classmethod
    def format_table(cls, table_dict: dict, tab_spacing="\t") -> str:
        """Takes a table_dict and formats it into a problerly formatted Alembic table."""

        table_name = table_dict.get("table_name")
        formatted_columns = f",\n{tab_spacing}".join(
            [cls.format_column(col) for col in table_dict.get("columns")]
        )

        return table_name, f"""\
op.create_table(
{tab_spacing}'{table_name}',
{tab_spacing}{formatted_columns}
)
"""

    @classmethod
    def convert(cls, ddl: str, tab_spacing="    ") -> str:
        """Converts raw ddl to an Alembic string."""

        cleaned_ddl = cls.clean_ddl(ddl)
        parsed_table = DDLParser(cleaned_ddl.replace("`", "")).run()
        
        # if the parsing fails, return "FAILED"
        if not parsed_table:
            return "FAILED"
        else:
            parsed_table = parsed_table[0]
        
        # Convert List to String: (for printing)
        #return cls.format_table(parsed_table, tab_spacing=tab_spacing)
        
        # Return (tablename, formatted_table): (for selective printing)
        return cls.format_table(parsed_table, tab_spacing=tab_spacing)
