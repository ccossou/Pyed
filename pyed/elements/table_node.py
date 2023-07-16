import logging
import sys

from .generic_node import GenericNode

LOG = logging.getLogger(__name__)


class TableNode(GenericNode):
    node_type = "GenericNode"

    default_table_style = dict(alignment="center", backgroundColor=None, verticalTextPosition="top")

    def __init__(self, name, table, title_style={}, table_style={}, **kwargs):
        """
        TableNode is a hack that uses GenericNode (list node) and convert a given table into HTML.

        Table Node only works if <html> is next to the label start. If there's a new line in between, it won't work. As
        a consequence, I had to get rid of minidom pretty print to make it work from scratch.

        table = [
        ("Rows", "Name", "Unit"),
        ("Row 0", "toto", "str"),
        ("Row 1", 123, "int"),
        ]

        :param str name: Node Name (title)
        :param list(tuple(str)) table: List of lines. First line is header. All lines must have the same length.
        :param dict title_style: Label Style for the TableNode title
        :param dict table_style: Label Style for the table Label
        :param dict kwargs: Extra parameters are passed to the GenericNode parent class
        """

        self.table = table
        self.check_table()

        # Add an html version of our table as a description in GenericNode
        html_txt = self.make_html_table(table)

        self.title_style = title_style

        self.table_style = self.default_table_style.copy()  # Default description
        self.table_style.update(table_style)  # custom for description

        super().__init__(name, description=html_txt, title_style=self.title_style, desc_style=self.table_style,
                         **kwargs)

    def make_html_table(self, table):
        """
        Convert table values into an HTML table.

        :param list(tuple(str)) table: List of lines. First line is header. All lines must have the same length.

        :return: html code corresponding to the input table
        :rtype: str
        """
        html_txt = "<html>"
        html_txt += "<table style='border:0px solid black;border-collapse: collapse;' cellspacing='0' tablespacing='0'>"

        cell_style_prefix = "style='border:1px solid black;border-collapse: collapse;"

        header = True
        for j, line in enumerate(table):
            html_txt += "<tr>"

            if header:
                cell = "th"
                header = False
            else:
                cell = "td"

            for i, text in enumerate(line):
                # Adapt cell style for first column and first line
                cell_style = cell_style_prefix
                if i != 0:
                    cell_style += "border-left:0;"
                if j != 0:
                    cell_style += "border-top:0;"
                cell_style += "'"

                html_txt += f"<{cell} {cell_style}>{text}</{cell}>"

            html_txt += "</tr>"

        html_txt += "</table></html>"

        return html_txt


    def check_table(self):
        """
        Check if self.table is valid
        """
        if not isinstance(self.table, list):
            raise TypeError(f"Input table need to be a list, got '{type(self.table)}' instead.")

        n_elem = None
        for line in self.table:
            line_len = len(line)
            if n_elem is None:
                n_elem = line_len
            else:
                if n_elem != line_len:
                    raise ValueError(f"All lines in table need the same number of elements")


    def to_xml(self):
        """
        Create the corresponding XML object.

        The main creation is done in the parent class Node. Only extra steps are done here.

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """
        # Generic Node conversion
        super().to_xml()

        return self._ET_node
