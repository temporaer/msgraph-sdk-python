from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class VdbPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new vdbPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cost property
        self._cost: Optional[json.Json] = None
        # The endPeriod property
        self._end_period: Optional[json.Json] = None
        # The factor property
        self._factor: Optional[json.Json] = None
        # The life property
        self._life: Optional[json.Json] = None
        # The noSwitch property
        self._no_switch: Optional[json.Json] = None
        # The salvage property
        self._salvage: Optional[json.Json] = None
        # The startPeriod property
        self._start_period: Optional[json.Json] = None
    
    @property
    def cost(self,) -> Optional[json.Json]:
        """
        Gets the cost property value. The cost property
        Returns: Optional[json.Json]
        """
        return self._cost
    
    @cost.setter
    def cost(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the cost property value. The cost property
        Args:
            value: Value to set for the cost property.
        """
        self._cost = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VdbPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: VdbPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return VdbPostRequestBody()
    
    @property
    def end_period(self,) -> Optional[json.Json]:
        """
        Gets the endPeriod property value. The endPeriod property
        Returns: Optional[json.Json]
        """
        return self._end_period
    
    @end_period.setter
    def end_period(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the endPeriod property value. The endPeriod property
        Args:
            value: Value to set for the end_period property.
        """
        self._end_period = value
    
    @property
    def factor(self,) -> Optional[json.Json]:
        """
        Gets the factor property value. The factor property
        Returns: Optional[json.Json]
        """
        return self._factor
    
    @factor.setter
    def factor(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the factor property value. The factor property
        Args:
            value: Value to set for the factor property.
        """
        self._factor = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cost": lambda n : setattr(self, 'cost', n.get_object_value(json.Json)),
            "endPeriod": lambda n : setattr(self, 'end_period', n.get_object_value(json.Json)),
            "factor": lambda n : setattr(self, 'factor', n.get_object_value(json.Json)),
            "life": lambda n : setattr(self, 'life', n.get_object_value(json.Json)),
            "noSwitch": lambda n : setattr(self, 'no_switch', n.get_object_value(json.Json)),
            "salvage": lambda n : setattr(self, 'salvage', n.get_object_value(json.Json)),
            "startPeriod": lambda n : setattr(self, 'start_period', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def life(self,) -> Optional[json.Json]:
        """
        Gets the life property value. The life property
        Returns: Optional[json.Json]
        """
        return self._life
    
    @life.setter
    def life(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the life property value. The life property
        Args:
            value: Value to set for the life property.
        """
        self._life = value
    
    @property
    def no_switch(self,) -> Optional[json.Json]:
        """
        Gets the noSwitch property value. The noSwitch property
        Returns: Optional[json.Json]
        """
        return self._no_switch
    
    @no_switch.setter
    def no_switch(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the noSwitch property value. The noSwitch property
        Args:
            value: Value to set for the no_switch property.
        """
        self._no_switch = value
    
    @property
    def salvage(self,) -> Optional[json.Json]:
        """
        Gets the salvage property value. The salvage property
        Returns: Optional[json.Json]
        """
        return self._salvage
    
    @salvage.setter
    def salvage(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the salvage property value. The salvage property
        Args:
            value: Value to set for the salvage property.
        """
        self._salvage = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("cost", self.cost)
        writer.write_object_value("endPeriod", self.end_period)
        writer.write_object_value("factor", self.factor)
        writer.write_object_value("life", self.life)
        writer.write_object_value("noSwitch", self.no_switch)
        writer.write_object_value("salvage", self.salvage)
        writer.write_object_value("startPeriod", self.start_period)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_period(self,) -> Optional[json.Json]:
        """
        Gets the startPeriod property value. The startPeriod property
        Returns: Optional[json.Json]
        """
        return self._start_period
    
    @start_period.setter
    def start_period(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the startPeriod property value. The startPeriod property
        Args:
            value: Value to set for the start_period property.
        """
        self._start_period = value
    
