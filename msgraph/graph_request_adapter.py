from typing import Dict, Optional
import httpx
from kiota_abstractions.authentication import AuthenticationProvider
from kiota_http.middleware.options import UrlReplaceHandlerOptions
from msgraph_core import APIVersion, BaseGraphRequestAdapter, GraphClientFactory
from msgraph_core.middleware.options import GraphTelemetryHandlerOption

from ._version import VERSION

options = {
    UrlReplaceHandlerOption.get_key(): UrlReplaceHandlerOptions(
        enabled = True,
        replacement_pairs = {"/users/me-token-to-replace": "/me"}
    ),
    GraphTelemetryHandlerOption.get_key(): GraphTelemetryHandlerOption(
        api_version=APIVersion.v1,
        sdk_version=VERSION)
}


class GraphRequestAdapter(BaseGraphRequestAdapter):
    def __init__(self, auth_provider: AuthenticationProvider,
                 client: Optional[httpx.AsyncClient] = GraphClientFactory.create_with_default_middleware(options=options)) -> None:
        super().__init__(auth_provider, http_client=client)

