from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import organizational_branding_localization
    from ......models.o_data_errors import o_data_error
    from .background_image import background_image_request_builder
    from .banner_logo import banner_logo_request_builder
    from .square_logo import square_logo_request_builder

class OrganizationalBrandingLocalizationItemRequestBuilder():
    """
    Provides operations to manage the localizations property of the microsoft.graph.organizationalBranding entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OrganizationalBrandingLocalizationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/organization/{organization%2Did}/branding/localizations/{organizationalBrandingLocalization%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property localizations for organization
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[organizational_branding_localization.OrganizationalBrandingLocalization]:
        """
        Add different branding based on a locale.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organizational_branding_localization.OrganizationalBrandingLocalization]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import organizational_branding_localization

        return await self.request_adapter.send_async(request_info, organizational_branding_localization.OrganizationalBrandingLocalization, error_mapping)
    
    async def patch(self,body: Optional[organizational_branding_localization.OrganizationalBrandingLocalization] = None, request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[organizational_branding_localization.OrganizationalBrandingLocalization]:
        """
        Update the navigation property localizations in organization
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organizational_branding_localization.OrganizationalBrandingLocalization]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import organizational_branding_localization

        return await self.request_adapter.send_async(request_info, organizational_branding_localization.OrganizationalBrandingLocalization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property localizations for organization
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Add different branding based on a locale.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[organizational_branding_localization.OrganizationalBrandingLocalization] = None, request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property localizations in organization
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def background_image(self) -> background_image_request_builder.BackgroundImageRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .background_image import background_image_request_builder

        return background_image_request_builder.BackgroundImageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def banner_logo(self) -> banner_logo_request_builder.BannerLogoRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .banner_logo import banner_logo_request_builder

        return banner_logo_request_builder.BannerLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def square_logo(self) -> square_logo_request_builder.SquareLogoRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .square_logo import square_logo_request_builder

        return square_logo_request_builder.SquareLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters():
        """
        Add different branding based on a locale.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OrganizationalBrandingLocalizationItemRequestBuilder.OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

