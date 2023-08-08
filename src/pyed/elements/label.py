import logging
import xml.etree.ElementTree as ET

from ..core import constants
from ..core import utils

LOG = logging.getLogger(__name__)


class Label:
    allowed_tags = ["y:NodeLabel", "y:EdgeLabel"]

    # For each Label tag, placement model allowed
    allowed_models = {
        "y:NodeLabel": ["internal", "corners", "sandwich", "sides", "eight_pos", "free", "custom"],
        "y:EdgeLabel": ["two_pos", "centered", "six_pos", "three_center", "center_slider", "side_slider", "free"],
    }

    def __init__(self, text, tag, height="30", width=None, alignment="center", fontFamily="Dialog",
                 fontSize="12", fontStyle="plain", underlinedText="false", textColor="#000000", iconTextGap="4",
                 visible="true", lineColor=None, backgroundColor=None, modelName="free", modelPosition="anywhere",
                 autoSizePolicy=None, **kwargs):
        """

        :param str text:
        :param str tag: Type of Label, either "y:NodeLabel" or "y:EdgeLabel"
        :param height:
        :param width:
        :param str alignment:
        :param str fontFamily:
        :param str fontSize:
        :param str fontStyle:
        :param str underlinedText: 'true' or 'false'
        :param str textColor:
        :param str iconTextGap: integer
        :param str visible:
        :param str lineColor:
        :param str backgroundColor:
        :param str modelName:
        :param str modelPosition:
        :param str autoSizePolicy:
        :param kwargs: Extra parameter can be passed as long as they are valid xml parameters for the current tag label.
        """

        self._text = text

        utils.check_value("tag", tag, self.allowed_tags)
        self.tag = tag

        # Initialize dictionary for parameters
        self._params = {}
        self.updateParam("alignment", alignment, constants.horizontal_alignments)
        self.updateParam("fontStyle", fontStyle, constants.font_styles)
        self.updateParam("fontFamily", fontFamily)
        self.updateParam("iconTextGap", iconTextGap)
        self.updateParam("fontSize", fontSize)
        self.updateParam("textColor", textColor)
        self.updateParam("visible", visible.lower(), ["true", "false"])
        self.updateParam("underlinedText", underlinedText.lower(), ["true", "false"])
        self.updateParam("width", width)
        self.updateParam("height", height)
        self.updateParam("lineColor", lineColor)
        self.updateParam("backgroundColor", backgroundColor)
        self.updateParam("modelName", modelName, self.allowed_models[tag])
        self.updateParam("modelPosition", modelPosition, constants.valid_model_params[modelName])

        if tag == "y:EdgeLabel" and autoSizePolicy is not None:
            raise ValueError(f"Can't use parameter 'autoSizePolicy' with {self.tag}")
        self.updateParam("autoSizePolicy", autoSizePolicy, constants.autoSizePolicy_values)

        for key, value in kwargs.items():
            self.updateParam(key, value)

    def updateParam(self, parameter_name, value, validValues=None):
        """
        Add parameter to Label instance. If value is None, add nothing, if invalid value is found, raise a ValueError

        :param str parameter_name:
        :param value:
        :param list validValues:

        :return: True or False, if value was updated or not.
        :rtype: bool
        """
        if value is None:
            return False
        utils.check_value(parameter_name, value, validValues)

        self._params[parameter_name] = value
        return True

    def to_xml(self, parent):
        """
        Create the corresponding XML object

        :param Element parent: Parent xml object

        :return: child object created
        :rtype: xml.etree.ElementTree.Element
        """

        # set parameter just before making the xml node, to make sure the value is accurate
        if "backgroundColor" in self._params and self._params["backgroundColor"] is not None:
            has_background_color = "true"
        else:
            has_background_color = "false"
        self.updateParam("hasBackgroundColor", has_background_color, ["true", "false"])

        label = ET.SubElement(parent, self.tag, **self._params)
        label.text = self._text
        return label
