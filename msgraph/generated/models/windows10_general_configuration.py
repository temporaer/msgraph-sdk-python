from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import defender_cloud_block_level_type, defender_detected_malware_actions, defender_monitor_file_activity, defender_prompt_for_sample_submission, defender_scan_type, device_configuration, diagnostic_data_submission_mode, edge_cookie_policy, edge_search_engine_base, required_password_type, safe_search_filter_type, state_management_setting, visibility_setting, weekly_schedule, windows10_network_proxy_server, windows_spotlight_enablement_settings, windows_start_menu_app_list_visibility_type, windows_start_menu_mode_type

from . import device_configuration

class Windows10GeneralConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10GeneralConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10GeneralConfiguration"
        # Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
        self._accounts_block_adding_non_microsoft_account_email: Optional[bool] = None
        # Indicates whether or not to block the user from selecting an AntiTheft mode preference (Windows 10 Mobile only).
        self._anti_theft_mode_blocked: Optional[bool] = None
        # State Management Setting.
        self._apps_allow_trusted_apps_sideloading: Optional[state_management_setting.StateManagementSetting] = None
        # Indicates whether or not to disable the launch of all apps from Windows Store that came pre-installed or were downloaded.
        self._apps_block_windows_store_originated_apps: Optional[bool] = None
        # Specify a list of allowed Bluetooth services and profiles in hex formatted strings.
        self._bluetooth_allowed_services: Optional[List[str]] = None
        # Whether or not to Block the user from using bluetooth advertising.
        self._bluetooth_block_advertising: Optional[bool] = None
        # Whether or not to Block the user from using bluetooth discoverable mode.
        self._bluetooth_block_discoverable_mode: Optional[bool] = None
        # Whether or not to block specific bundled Bluetooth peripherals to automatically pair with the host device.
        self._bluetooth_block_pre_pairing: Optional[bool] = None
        # Whether or not to Block the user from using bluetooth.
        self._bluetooth_blocked: Optional[bool] = None
        # Whether or not to Block the user from accessing the camera of the device.
        self._camera_blocked: Optional[bool] = None
        # Whether or not to Block the user from using data over cellular while roaming.
        self._cellular_block_data_when_roaming: Optional[bool] = None
        # Whether or not to Block the user from using VPN over cellular.
        self._cellular_block_vpn: Optional[bool] = None
        # Whether or not to Block the user from using VPN when roaming over cellular.
        self._cellular_block_vpn_when_roaming: Optional[bool] = None
        # Whether or not to Block the user from doing manual root certificate installation.
        self._certificates_block_manual_root_certificate_installation: Optional[bool] = None
        # Whether or not to block Connected Devices Service which enables discovery and connection to other devices, remote messaging, remote app sessions and other cross-device experiences.
        self._connected_devices_service_blocked: Optional[bool] = None
        # Whether or not to Block the user from using copy paste.
        self._copy_paste_blocked: Optional[bool] = None
        # Whether or not to Block the user from using Cortana.
        self._cortana_blocked: Optional[bool] = None
        # Whether or not to block end user access to Defender.
        self._defender_block_end_user_access: Optional[bool] = None
        # Possible values of Cloud Block Level
        self._defender_cloud_block_level: Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType] = None
        # Number of days before deleting quarantined malware. Valid values 0 to 90
        self._defender_days_before_deleting_quarantined_malware: Optional[int] = None
        # Gets or sets Defender’s actions to take on detected Malware per threat level.
        self._defender_detected_malware_actions: Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions] = None
        # File extensions to exclude from scans and real time protection.
        self._defender_file_extensions_to_exclude: Optional[List[str]] = None
        # Files and folder to exclude from scans and real time protection.
        self._defender_files_and_folders_to_exclude: Optional[List[str]] = None
        # Possible values for monitoring file activity.
        self._defender_monitor_file_activity: Optional[defender_monitor_file_activity.DefenderMonitorFileActivity] = None
        # Processes to exclude from scans and real time protection.
        self._defender_processes_to_exclude: Optional[List[str]] = None
        # Possible values for prompting user for samples submission.
        self._defender_prompt_for_sample_submission: Optional[defender_prompt_for_sample_submission.DefenderPromptForSampleSubmission] = None
        # Indicates whether or not to require behavior monitoring.
        self._defender_require_behavior_monitoring: Optional[bool] = None
        # Indicates whether or not to require cloud protection.
        self._defender_require_cloud_protection: Optional[bool] = None
        # Indicates whether or not to require network inspection system.
        self._defender_require_network_inspection_system: Optional[bool] = None
        # Indicates whether or not to require real time monitoring.
        self._defender_require_real_time_monitoring: Optional[bool] = None
        # Indicates whether or not to scan archive files.
        self._defender_scan_archive_files: Optional[bool] = None
        # Indicates whether or not to scan downloads.
        self._defender_scan_downloads: Optional[bool] = None
        # Indicates whether or not to scan incoming mail messages.
        self._defender_scan_incoming_mail: Optional[bool] = None
        # Indicates whether or not to scan mapped network drives during full scan.
        self._defender_scan_mapped_network_drives_during_full_scan: Optional[bool] = None
        # Max CPU usage percentage during scan. Valid values 0 to 100
        self._defender_scan_max_cpu: Optional[int] = None
        # Indicates whether or not to scan files opened from a network folder.
        self._defender_scan_network_files: Optional[bool] = None
        # Indicates whether or not to scan removable drives during full scan.
        self._defender_scan_removable_drives_during_full_scan: Optional[bool] = None
        # Indicates whether or not to scan scripts loaded in Internet Explorer browser.
        self._defender_scan_scripts_loaded_in_internet_explorer: Optional[bool] = None
        # Possible values for system scan type.
        self._defender_scan_type: Optional[defender_scan_type.DefenderScanType] = None
        # The time to perform a daily quick scan.
        self._defender_scheduled_quick_scan_time: Optional[time] = None
        # The defender time for the system scan.
        self._defender_scheduled_scan_time: Optional[time] = None
        # The signature update interval in hours. Specify 0 not to check. Valid values 0 to 24
        self._defender_signature_update_interval_in_hours: Optional[int] = None
        # Possible values for a weekly schedule.
        self._defender_system_scan_schedule: Optional[weekly_schedule.WeeklySchedule] = None
        # State Management Setting.
        self._developer_unlock_setting: Optional[state_management_setting.StateManagementSetting] = None
        # Indicates whether or not to Block the user from resetting their phone.
        self._device_management_block_factory_reset_on_mobile: Optional[bool] = None
        # Indicates whether or not to Block the user from doing manual un-enrollment from device management.
        self._device_management_block_manual_unenroll: Optional[bool] = None
        # Allow the device to send diagnostic and usage telemetry data, such as Watson.
        self._diagnostics_data_submission_mode: Optional[diagnostic_data_submission_mode.DiagnosticDataSubmissionMode] = None
        # Allow users to change Start pages on Edge. Use the EdgeHomepageUrls to specify the Start pages that the user would see by default when they open Edge.
        self._edge_allow_start_pages_modification: Optional[bool] = None
        # Indicates whether or not to prevent access to about flags on Edge browser.
        self._edge_block_access_to_about_flags: Optional[bool] = None
        # Block the address bar dropdown functionality in Microsoft Edge. Disable this settings to minimize network connections from Microsoft Edge to Microsoft services.
        self._edge_block_address_bar_dropdown: Optional[bool] = None
        # Indicates whether or not to block auto fill.
        self._edge_block_autofill: Optional[bool] = None
        # Block Microsoft compatibility list in Microsoft Edge. This list from Microsoft helps Edge properly display sites with known compatibility issues.
        self._edge_block_compatibility_list: Optional[bool] = None
        # Indicates whether or not to block developer tools in the Edge browser.
        self._edge_block_developer_tools: Optional[bool] = None
        # Indicates whether or not to block extensions in the Edge browser.
        self._edge_block_extensions: Optional[bool] = None
        # Indicates whether or not to block InPrivate browsing on corporate networks, in the Edge browser.
        self._edge_block_in_private_browsing: Optional[bool] = None
        # Indicates whether or not to Block the user from using JavaScript.
        self._edge_block_java_script: Optional[bool] = None
        # Block the collection of information by Microsoft for live tile creation when users pin a site to Start from Microsoft Edge.
        self._edge_block_live_tile_data_collection: Optional[bool] = None
        # Indicates whether or not to Block password manager.
        self._edge_block_password_manager: Optional[bool] = None
        # Indicates whether or not to block popups.
        self._edge_block_popups: Optional[bool] = None
        # Indicates whether or not to block the user from using the search suggestions in the address bar.
        self._edge_block_search_suggestions: Optional[bool] = None
        # Indicates whether or not to Block the user from sending the do not track header.
        self._edge_block_sending_do_not_track_header: Optional[bool] = None
        # Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer. Note: the name of this property is misleading; the property is obsolete, use EdgeSendIntranetTrafficToInternetExplorer instead.
        self._edge_block_sending_intranet_traffic_to_internet_explorer: Optional[bool] = None
        # Indicates whether or not to Block the user from using the Edge browser.
        self._edge_blocked: Optional[bool] = None
        # Clear browsing data on exiting Microsoft Edge.
        self._edge_clear_browsing_data_on_exit: Optional[bool] = None
        # Possible values to specify which cookies are allowed in Microsoft Edge.
        self._edge_cookie_policy: Optional[edge_cookie_policy.EdgeCookiePolicy] = None
        # Block the Microsoft web page that opens on the first use of Microsoft Edge. This policy allows enterprises, like those enrolled in zero emissions configurations, to block this page.
        self._edge_disable_first_run_page: Optional[bool] = None
        # Indicates the enterprise mode site list location. Could be a local file, local network or http location.
        self._edge_enterprise_mode_site_list_location: Optional[str] = None
        # The first run URL for when Edge browser is opened for the first time.
        self._edge_first_run_url: Optional[str] = None
        # The list of URLs for homepages shodwn on MDM-enrolled devices on Edge browser.
        self._edge_homepage_urls: Optional[List[str]] = None
        # Indicates whether or not to Require the user to use the smart screen filter.
        self._edge_require_smart_screen: Optional[bool] = None
        # Allows IT admins to set a default search engine for MDM-Controlled devices. Users can override this and change their default search engine provided the AllowSearchEngineCustomization policy is not set.
        self._edge_search_engine: Optional[edge_search_engine_base.EdgeSearchEngineBase] = None
        # Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer.
        self._edge_send_intranet_traffic_to_internet_explorer: Optional[bool] = None
        # Enable favorites sync between Internet Explorer and Microsoft Edge. Additions, deletions, modifications and order changes to favorites are shared between browsers.
        self._edge_sync_favorites_with_internet_explorer: Optional[bool] = None
        # Endpoint for discovering cloud printers.
        self._enterprise_cloud_print_discovery_end_point: Optional[str] = None
        # Maximum number of printers that should be queried from a discovery endpoint. This is a mobile only setting. Valid values 1 to 65535
        self._enterprise_cloud_print_discovery_max_limit: Optional[int] = None
        # OAuth resource URI for printer discovery service as configured in Azure portal.
        self._enterprise_cloud_print_mopria_discovery_resource_identifier: Optional[str] = None
        # Authentication endpoint for acquiring OAuth tokens.
        self._enterprise_cloud_print_o_auth_authority: Optional[str] = None
        # GUID of a client application authorized to retrieve OAuth tokens from the OAuth Authority.
        self._enterprise_cloud_print_o_auth_client_identifier: Optional[str] = None
        # OAuth resource URI for print service as configured in the Azure portal.
        self._enterprise_cloud_print_resource_identifier: Optional[str] = None
        # Indicates whether or not to enable device discovery UX.
        self._experience_block_device_discovery: Optional[bool] = None
        # Indicates whether or not to allow the error dialog from displaying if no SIM card is detected.
        self._experience_block_error_dialog_when_no_s_i_m: Optional[bool] = None
        # Indicates whether or not to enable task switching on the device.
        self._experience_block_task_switcher: Optional[bool] = None
        # Indicates whether or not to block DVR and broadcasting.
        self._game_dvr_blocked: Optional[bool] = None
        # Indicates whether or not to Block the user from using internet sharing.
        self._internet_sharing_blocked: Optional[bool] = None
        # Indicates whether or not to Block the user from location services.
        self._location_services_blocked: Optional[bool] = None
        # Specify whether to show a user-configurable setting to control the screen timeout while on the lock screen of Windows 10 Mobile devices. If this policy is set to Allow, the value set by lockScreenTimeoutInSeconds is ignored.
        self._lock_screen_allow_timeout_configuration: Optional[bool] = None
        # Indicates whether or not to block action center notifications over lock screen.
        self._lock_screen_block_action_center_notifications: Optional[bool] = None
        # Indicates whether or not the user can interact with Cortana using speech while the system is locked.
        self._lock_screen_block_cortana: Optional[bool] = None
        # Indicates whether to allow toast notifications above the device lock screen.
        self._lock_screen_block_toast_notifications: Optional[bool] = None
        # Set the duration (in seconds) from the screen locking to the screen turning off for Windows 10 Mobile devices. Supported values are 11-1800. Valid values 11 to 1800
        self._lock_screen_timeout_in_seconds: Optional[int] = None
        # Disables the ability to quickly switch between users that are logged on simultaneously without logging off.
        self._logon_block_fast_user_switching: Optional[bool] = None
        # Indicates whether or not to Block Microsoft account settings sync.
        self._microsoft_account_block_settings_sync: Optional[bool] = None
        # Indicates whether or not to Block a Microsoft account.
        self._microsoft_account_blocked: Optional[bool] = None
        # If set, proxy settings will be applied to all processes and accounts in the device. Otherwise, it will be applied to the user account that’s enrolled into MDM.
        self._network_proxy_apply_settings_device_wide: Optional[bool] = None
        # Address to the proxy auto-config (PAC) script you want to use.
        self._network_proxy_automatic_configuration_url: Optional[str] = None
        # Disable automatic detection of settings. If enabled, the system will try to find the path to a proxy auto-config (PAC) script.
        self._network_proxy_disable_auto_detect: Optional[bool] = None
        # Specifies manual proxy server settings.
        self._network_proxy_server: Optional[windows10_network_proxy_server.Windows10NetworkProxyServer] = None
        # Indicates whether or not to Block the user from using near field communication.
        self._nfc_blocked: Optional[bool] = None
        # Gets or sets a value allowing IT admins to prevent apps and features from working with files on OneDrive.
        self._one_drive_disable_file_sync: Optional[bool] = None
        # Specify whether PINs or passwords such as '1111' or '1234' are allowed. For Windows 10 desktops, it also controls the use of picture passwords.
        self._password_block_simple: Optional[bool] = None
        # The password expiration in days. Valid values 0 to 730
        self._password_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._password_minimum_character_set_count: Optional[int] = None
        # The minimum password length. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # The minutes of inactivity before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # The number of previous passwords to prevent reuse of. Valid values 0 to 50
        self._password_previous_password_block_count: Optional[int] = None
        # Indicates whether or not to require a password upon resuming from an idle state.
        self._password_require_when_resume_from_idle_state: Optional[bool] = None
        # Indicates whether or not to require the user to have a password.
        self._password_required: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # The number of sign in failures before factory reset. Valid values 0 to 999
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # A http or https Url to a jpg, jpeg or png image that needs to be downloaded and used as the Desktop Image or a file Url to a local image on the file system that needs to used as the Desktop Image.
        self._personalization_desktop_image_url: Optional[str] = None
        # A http or https Url to a jpg, jpeg or png image that neeeds to be downloaded and used as the Lock Screen Image or a file Url to a local image on the file system that needs to be used as the Lock Screen Image.
        self._personalization_lock_screen_image_url: Optional[str] = None
        # State Management Setting.
        self._privacy_advertising_id: Optional[state_management_setting.StateManagementSetting] = None
        # Indicates whether or not to allow the automatic acceptance of the pairing and privacy user consent dialog when launching apps.
        self._privacy_auto_accept_pairing_and_consent_prompts: Optional[bool] = None
        # Indicates whether or not to block the usage of cloud based speech services for Cortana, Dictation, or Store applications.
        self._privacy_block_input_personalization: Optional[bool] = None
        # Indicates whether or not to Block the user from reset protection mode.
        self._reset_protection_mode_blocked: Optional[bool] = None
        # Specifies what level of safe search (filtering adult content) is required
        self._safe_search_filter: Optional[safe_search_filter_type.SafeSearchFilterType] = None
        # Indicates whether or not to Block the user from taking Screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Specifies if search can use diacritics.
        self._search_block_diacritics: Optional[bool] = None
        # Specifies whether to use automatic language detection when indexing content and properties.
        self._search_disable_auto_language_detection: Optional[bool] = None
        # Indicates whether or not to disable the search indexer backoff feature.
        self._search_disable_indexer_backoff: Optional[bool] = None
        # Indicates whether or not to block indexing of WIP-protected items to prevent them from appearing in search results for Cortana or Explorer.
        self._search_disable_indexing_encrypted_items: Optional[bool] = None
        # Indicates whether or not to allow users to add locations on removable drives to libraries and to be indexed.
        self._search_disable_indexing_removable_drive: Optional[bool] = None
        # Specifies minimum amount of hard drive space on the same drive as the index location before indexing stops.
        self._search_enable_automatic_index_size_manangement: Optional[bool] = None
        # Indicates whether or not to block remote queries of this computer’s index.
        self._search_enable_remote_queries: Optional[bool] = None
        # Indicates whether or not to block access to Accounts in Settings app.
        self._settings_block_accounts_page: Optional[bool] = None
        # Indicates whether or not to block the user from installing provisioning packages.
        self._settings_block_add_provisioning_package: Optional[bool] = None
        # Indicates whether or not to block access to Apps in Settings app.
        self._settings_block_apps_page: Optional[bool] = None
        # Indicates whether or not to block the user from changing the language settings.
        self._settings_block_change_language: Optional[bool] = None
        # Indicates whether or not to block the user from changing power and sleep settings.
        self._settings_block_change_power_sleep: Optional[bool] = None
        # Indicates whether or not to block the user from changing the region settings.
        self._settings_block_change_region: Optional[bool] = None
        # Indicates whether or not to block the user from changing date and time settings.
        self._settings_block_change_system_time: Optional[bool] = None
        # Indicates whether or not to block access to Devices in Settings app.
        self._settings_block_devices_page: Optional[bool] = None
        # Indicates whether or not to block access to Ease of Access in Settings app.
        self._settings_block_ease_of_access_page: Optional[bool] = None
        # Indicates whether or not to block the user from editing the device name.
        self._settings_block_edit_device_name: Optional[bool] = None
        # Indicates whether or not to block access to Gaming in Settings app.
        self._settings_block_gaming_page: Optional[bool] = None
        # Indicates whether or not to block access to Network & Internet in Settings app.
        self._settings_block_network_internet_page: Optional[bool] = None
        # Indicates whether or not to block access to Personalization in Settings app.
        self._settings_block_personalization_page: Optional[bool] = None
        # Indicates whether or not to block access to Privacy in Settings app.
        self._settings_block_privacy_page: Optional[bool] = None
        # Indicates whether or not to block the runtime configuration agent from removing provisioning packages.
        self._settings_block_remove_provisioning_package: Optional[bool] = None
        # Indicates whether or not to block access to Settings app.
        self._settings_block_settings_app: Optional[bool] = None
        # Indicates whether or not to block access to System in Settings app.
        self._settings_block_system_page: Optional[bool] = None
        # Indicates whether or not to block access to Time & Language in Settings app.
        self._settings_block_time_language_page: Optional[bool] = None
        # Indicates whether or not to block access to Update & Security in Settings app.
        self._settings_block_update_security_page: Optional[bool] = None
        # Indicates whether or not to block multiple users of the same app to share data.
        self._shared_user_app_data_allowed: Optional[bool] = None
        # Indicates whether or not users can override SmartScreen Filter warnings about potentially malicious websites.
        self._smart_screen_block_prompt_override: Optional[bool] = None
        # Indicates whether or not users can override the SmartScreen Filter warnings about downloading unverified files
        self._smart_screen_block_prompt_override_for_files: Optional[bool] = None
        # This property will be deprecated in July 2019 and will be replaced by property SmartScreenAppInstallControl. Allows IT Admins to control whether users are allowed to install apps from places other than the Store.
        self._smart_screen_enable_app_install_control: Optional[bool] = None
        # Indicates whether or not to block the user from unpinning apps from taskbar.
        self._start_block_unpinning_apps_from_taskbar: Optional[bool] = None
        # Type of start menu app list visibility.
        self._start_menu_app_list_visibility: Optional[windows_start_menu_app_list_visibility_type.WindowsStartMenuAppListVisibilityType] = None
        # Enabling this policy hides the change account setting from appearing in the user tile in the start menu.
        self._start_menu_hide_change_account_settings: Optional[bool] = None
        # Enabling this policy hides the most used apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
        self._start_menu_hide_frequently_used_apps: Optional[bool] = None
        # Enabling this policy hides hibernate from appearing in the power button in the start menu.
        self._start_menu_hide_hibernate: Optional[bool] = None
        # Enabling this policy hides lock from appearing in the user tile in the start menu.
        self._start_menu_hide_lock: Optional[bool] = None
        # Enabling this policy hides the power button from appearing in the start menu.
        self._start_menu_hide_power_button: Optional[bool] = None
        # Enabling this policy hides recent jump lists from appearing on the start menu/taskbar and disables the corresponding toggle in the Settings app.
        self._start_menu_hide_recent_jump_lists: Optional[bool] = None
        # Enabling this policy hides recently added apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
        self._start_menu_hide_recently_added_apps: Optional[bool] = None
        # Enabling this policy hides 'Restart/Update and Restart' from appearing in the power button in the start menu.
        self._start_menu_hide_restart_options: Optional[bool] = None
        # Enabling this policy hides shut down/update and shut down from appearing in the power button in the start menu.
        self._start_menu_hide_shut_down: Optional[bool] = None
        # Enabling this policy hides sign out from appearing in the user tile in the start menu.
        self._start_menu_hide_sign_out: Optional[bool] = None
        # Enabling this policy hides sleep from appearing in the power button in the start menu.
        self._start_menu_hide_sleep: Optional[bool] = None
        # Enabling this policy hides switch account from appearing in the user tile in the start menu.
        self._start_menu_hide_switch_account: Optional[bool] = None
        # Enabling this policy hides the user tile from appearing in the start menu.
        self._start_menu_hide_user_tile: Optional[bool] = None
        # This policy setting allows you to import Edge assets to be used with startMenuLayoutXml policy. Start layout can contain secondary tile from Edge app which looks for Edge local asset file. Edge local asset would not exist and cause Edge secondary tile to appear empty in this case. This policy only gets applied when startMenuLayoutXml policy is modified. The value should be a UTF-8 Base64 encoded byte array.
        self._start_menu_layout_edge_assets_xml: Optional[bytes] = None
        # Allows admins to override the default Start menu layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in a UTF8 encoded byte array format.
        self._start_menu_layout_xml: Optional[bytes] = None
        # Type of display modes for the start menu.
        self._start_menu_mode: Optional[windows_start_menu_mode_type.WindowsStartMenuModeType] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_documents: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_downloads: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_file_explorer: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_home_group: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_music: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_network: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_personal_folder: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_pictures: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_settings: Optional[visibility_setting.VisibilitySetting] = None
        # Generic visibility state.
        self._start_menu_pinned_folder_videos: Optional[visibility_setting.VisibilitySetting] = None
        # Indicates whether or not to Block the user from using removable storage.
        self._storage_block_removable_storage: Optional[bool] = None
        # Indicating whether or not to require encryption on a mobile device.
        self._storage_require_mobile_device_encryption: Optional[bool] = None
        # Indicates whether application data is restricted to the system drive.
        self._storage_restrict_app_data_to_system_volume: Optional[bool] = None
        # Indicates whether the installation of applications is restricted to the system drive.
        self._storage_restrict_app_install_to_system_volume: Optional[bool] = None
        # Whether the device is required to connect to the network.
        self._tenant_lockdown_require_network_during_out_of_box_experience: Optional[bool] = None
        # Indicates whether or not to Block the user from USB connection.
        self._usb_blocked: Optional[bool] = None
        # Indicates whether or not to Block the user from voice recording.
        self._voice_recording_blocked: Optional[bool] = None
        # Indicates whether or not user's localhost IP address is displayed while making phone calls using the WebRTC
        self._web_rtc_block_localhost_ip_address: Optional[bool] = None
        # Indicating whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
        self._wi_fi_block_automatic_connect_hotspots: Optional[bool] = None
        # Indicates whether or not to Block the user from using Wi-Fi manual configuration.
        self._wi_fi_block_manual_configuration: Optional[bool] = None
        # Indicates whether or not to Block the user from using Wi-Fi.
        self._wi_fi_blocked: Optional[bool] = None
        # Specify how often devices scan for Wi-Fi networks. Supported values are 1-500, where 100 = default, and 500 = low frequency. Valid values 1 to 500
        self._wi_fi_scan_interval: Optional[int] = None
        # Allows IT admins to block experiences that are typically for consumers only, such as Start suggestions, Membership notifications, Post-OOBE app install and redirect tiles.
        self._windows_spotlight_block_consumer_specific_features: Optional[bool] = None
        # Block suggestions from Microsoft that show after each OS clean install, upgrade or in an on-going basis to introduce users to what is new or changed
        self._windows_spotlight_block_on_action_center: Optional[bool] = None
        # Block personalized content in Windows spotlight based on user’s device usage.
        self._windows_spotlight_block_tailored_experiences: Optional[bool] = None
        # Block third party content delivered via Windows Spotlight
        self._windows_spotlight_block_third_party_notifications: Optional[bool] = None
        # Block Windows Spotlight Windows welcome experience
        self._windows_spotlight_block_welcome_experience: Optional[bool] = None
        # Allows IT admins to turn off the popup of Windows Tips.
        self._windows_spotlight_block_windows_tips: Optional[bool] = None
        # Allows IT admins to turn off all Windows Spotlight features
        self._windows_spotlight_blocked: Optional[bool] = None
        # Allows IT admind to set a predefined default search engine for MDM-Controlled devices
        self._windows_spotlight_configure_on_lock_screen: Optional[windows_spotlight_enablement_settings.WindowsSpotlightEnablementSettings] = None
        # Indicates whether or not to block automatic update of apps from Windows Store.
        self._windows_store_block_auto_update: Optional[bool] = None
        # Indicates whether or not to Block the user from using the Windows store.
        self._windows_store_blocked: Optional[bool] = None
        # Indicates whether or not to enable Private Store Only.
        self._windows_store_enable_private_store_only: Optional[bool] = None
        # Indicates whether or not to allow other devices from discovering this PC for projection.
        self._wireless_display_block_projection_to_this_device: Optional[bool] = None
        # Indicates whether or not to allow user input from wireless display receiver.
        self._wireless_display_block_user_input_from_receiver: Optional[bool] = None
        # Indicates whether or not to require a PIN for new devices to initiate pairing.
        self._wireless_display_require_pin_for_pairing: Optional[bool] = None
    
    @property
    def accounts_block_adding_non_microsoft_account_email(self,) -> Optional[bool]:
        """
        Gets the accountsBlockAddingNonMicrosoftAccountEmail property value. Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
        Returns: Optional[bool]
        """
        return self._accounts_block_adding_non_microsoft_account_email
    
    @accounts_block_adding_non_microsoft_account_email.setter
    def accounts_block_adding_non_microsoft_account_email(self,value: Optional[bool] = None) -> None:
        """
        Sets the accountsBlockAddingNonMicrosoftAccountEmail property value. Indicates whether or not to Block the user from adding email accounts to the device that are not associated with a Microsoft account.
        Args:
            value: Value to set for the accounts_block_adding_non_microsoft_account_email property.
        """
        self._accounts_block_adding_non_microsoft_account_email = value
    
    @property
    def anti_theft_mode_blocked(self,) -> Optional[bool]:
        """
        Gets the antiTheftModeBlocked property value. Indicates whether or not to block the user from selecting an AntiTheft mode preference (Windows 10 Mobile only).
        Returns: Optional[bool]
        """
        return self._anti_theft_mode_blocked
    
    @anti_theft_mode_blocked.setter
    def anti_theft_mode_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the antiTheftModeBlocked property value. Indicates whether or not to block the user from selecting an AntiTheft mode preference (Windows 10 Mobile only).
        Args:
            value: Value to set for the anti_theft_mode_blocked property.
        """
        self._anti_theft_mode_blocked = value
    
    @property
    def apps_allow_trusted_apps_sideloading(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the appsAllowTrustedAppsSideloading property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._apps_allow_trusted_apps_sideloading
    
    @apps_allow_trusted_apps_sideloading.setter
    def apps_allow_trusted_apps_sideloading(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the appsAllowTrustedAppsSideloading property value. State Management Setting.
        Args:
            value: Value to set for the apps_allow_trusted_apps_sideloading property.
        """
        self._apps_allow_trusted_apps_sideloading = value
    
    @property
    def apps_block_windows_store_originated_apps(self,) -> Optional[bool]:
        """
        Gets the appsBlockWindowsStoreOriginatedApps property value. Indicates whether or not to disable the launch of all apps from Windows Store that came pre-installed or were downloaded.
        Returns: Optional[bool]
        """
        return self._apps_block_windows_store_originated_apps
    
    @apps_block_windows_store_originated_apps.setter
    def apps_block_windows_store_originated_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsBlockWindowsStoreOriginatedApps property value. Indicates whether or not to disable the launch of all apps from Windows Store that came pre-installed or were downloaded.
        Args:
            value: Value to set for the apps_block_windows_store_originated_apps property.
        """
        self._apps_block_windows_store_originated_apps = value
    
    @property
    def bluetooth_allowed_services(self,) -> Optional[List[str]]:
        """
        Gets the bluetoothAllowedServices property value. Specify a list of allowed Bluetooth services and profiles in hex formatted strings.
        Returns: Optional[List[str]]
        """
        return self._bluetooth_allowed_services
    
    @bluetooth_allowed_services.setter
    def bluetooth_allowed_services(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the bluetoothAllowedServices property value. Specify a list of allowed Bluetooth services and profiles in hex formatted strings.
        Args:
            value: Value to set for the bluetooth_allowed_services property.
        """
        self._bluetooth_allowed_services = value
    
    @property
    def bluetooth_block_advertising(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockAdvertising property value. Whether or not to Block the user from using bluetooth advertising.
        Returns: Optional[bool]
        """
        return self._bluetooth_block_advertising
    
    @bluetooth_block_advertising.setter
    def bluetooth_block_advertising(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockAdvertising property value. Whether or not to Block the user from using bluetooth advertising.
        Args:
            value: Value to set for the bluetooth_block_advertising property.
        """
        self._bluetooth_block_advertising = value
    
    @property
    def bluetooth_block_discoverable_mode(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockDiscoverableMode property value. Whether or not to Block the user from using bluetooth discoverable mode.
        Returns: Optional[bool]
        """
        return self._bluetooth_block_discoverable_mode
    
    @bluetooth_block_discoverable_mode.setter
    def bluetooth_block_discoverable_mode(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockDiscoverableMode property value. Whether or not to Block the user from using bluetooth discoverable mode.
        Args:
            value: Value to set for the bluetooth_block_discoverable_mode property.
        """
        self._bluetooth_block_discoverable_mode = value
    
    @property
    def bluetooth_block_pre_pairing(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlockPrePairing property value. Whether or not to block specific bundled Bluetooth peripherals to automatically pair with the host device.
        Returns: Optional[bool]
        """
        return self._bluetooth_block_pre_pairing
    
    @bluetooth_block_pre_pairing.setter
    def bluetooth_block_pre_pairing(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlockPrePairing property value. Whether or not to block specific bundled Bluetooth peripherals to automatically pair with the host device.
        Args:
            value: Value to set for the bluetooth_block_pre_pairing property.
        """
        self._bluetooth_block_pre_pairing = value
    
    @property
    def bluetooth_blocked(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlocked property value. Whether or not to Block the user from using bluetooth.
        Returns: Optional[bool]
        """
        return self._bluetooth_blocked
    
    @bluetooth_blocked.setter
    def bluetooth_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlocked property value. Whether or not to Block the user from using bluetooth.
        Args:
            value: Value to set for the bluetooth_blocked property.
        """
        self._bluetooth_blocked = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Whether or not to Block the user from accessing the camera of the device.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Whether or not to Block the user from accessing the camera of the device.
        Args:
            value: Value to set for the camera_blocked property.
        """
        self._camera_blocked = value
    
    @property
    def cellular_block_data_when_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockDataWhenRoaming property value. Whether or not to Block the user from using data over cellular while roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_data_when_roaming
    
    @cellular_block_data_when_roaming.setter
    def cellular_block_data_when_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockDataWhenRoaming property value. Whether or not to Block the user from using data over cellular while roaming.
        Args:
            value: Value to set for the cellular_block_data_when_roaming property.
        """
        self._cellular_block_data_when_roaming = value
    
    @property
    def cellular_block_vpn(self,) -> Optional[bool]:
        """
        Gets the cellularBlockVpn property value. Whether or not to Block the user from using VPN over cellular.
        Returns: Optional[bool]
        """
        return self._cellular_block_vpn
    
    @cellular_block_vpn.setter
    def cellular_block_vpn(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockVpn property value. Whether or not to Block the user from using VPN over cellular.
        Args:
            value: Value to set for the cellular_block_vpn property.
        """
        self._cellular_block_vpn = value
    
    @property
    def cellular_block_vpn_when_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockVpnWhenRoaming property value. Whether or not to Block the user from using VPN when roaming over cellular.
        Returns: Optional[bool]
        """
        return self._cellular_block_vpn_when_roaming
    
    @cellular_block_vpn_when_roaming.setter
    def cellular_block_vpn_when_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockVpnWhenRoaming property value. Whether or not to Block the user from using VPN when roaming over cellular.
        Args:
            value: Value to set for the cellular_block_vpn_when_roaming property.
        """
        self._cellular_block_vpn_when_roaming = value
    
    @property
    def certificates_block_manual_root_certificate_installation(self,) -> Optional[bool]:
        """
        Gets the certificatesBlockManualRootCertificateInstallation property value. Whether or not to Block the user from doing manual root certificate installation.
        Returns: Optional[bool]
        """
        return self._certificates_block_manual_root_certificate_installation
    
    @certificates_block_manual_root_certificate_installation.setter
    def certificates_block_manual_root_certificate_installation(self,value: Optional[bool] = None) -> None:
        """
        Sets the certificatesBlockManualRootCertificateInstallation property value. Whether or not to Block the user from doing manual root certificate installation.
        Args:
            value: Value to set for the certificates_block_manual_root_certificate_installation property.
        """
        self._certificates_block_manual_root_certificate_installation = value
    
    @property
    def connected_devices_service_blocked(self,) -> Optional[bool]:
        """
        Gets the connectedDevicesServiceBlocked property value. Whether or not to block Connected Devices Service which enables discovery and connection to other devices, remote messaging, remote app sessions and other cross-device experiences.
        Returns: Optional[bool]
        """
        return self._connected_devices_service_blocked
    
    @connected_devices_service_blocked.setter
    def connected_devices_service_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectedDevicesServiceBlocked property value. Whether or not to block Connected Devices Service which enables discovery and connection to other devices, remote messaging, remote app sessions and other cross-device experiences.
        Args:
            value: Value to set for the connected_devices_service_blocked property.
        """
        self._connected_devices_service_blocked = value
    
    @property
    def copy_paste_blocked(self,) -> Optional[bool]:
        """
        Gets the copyPasteBlocked property value. Whether or not to Block the user from using copy paste.
        Returns: Optional[bool]
        """
        return self._copy_paste_blocked
    
    @copy_paste_blocked.setter
    def copy_paste_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the copyPasteBlocked property value. Whether or not to Block the user from using copy paste.
        Args:
            value: Value to set for the copy_paste_blocked property.
        """
        self._copy_paste_blocked = value
    
    @property
    def cortana_blocked(self,) -> Optional[bool]:
        """
        Gets the cortanaBlocked property value. Whether or not to Block the user from using Cortana.
        Returns: Optional[bool]
        """
        return self._cortana_blocked
    
    @cortana_blocked.setter
    def cortana_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cortanaBlocked property value. Whether or not to Block the user from using Cortana.
        Args:
            value: Value to set for the cortana_blocked property.
        """
        self._cortana_blocked = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10GeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10GeneralConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10GeneralConfiguration()
    
    @property
    def defender_block_end_user_access(self,) -> Optional[bool]:
        """
        Gets the defenderBlockEndUserAccess property value. Whether or not to block end user access to Defender.
        Returns: Optional[bool]
        """
        return self._defender_block_end_user_access
    
    @defender_block_end_user_access.setter
    def defender_block_end_user_access(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderBlockEndUserAccess property value. Whether or not to block end user access to Defender.
        Args:
            value: Value to set for the defender_block_end_user_access property.
        """
        self._defender_block_end_user_access = value
    
    @property
    def defender_cloud_block_level(self,) -> Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType]:
        """
        Gets the defenderCloudBlockLevel property value. Possible values of Cloud Block Level
        Returns: Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType]
        """
        return self._defender_cloud_block_level
    
    @defender_cloud_block_level.setter
    def defender_cloud_block_level(self,value: Optional[defender_cloud_block_level_type.DefenderCloudBlockLevelType] = None) -> None:
        """
        Sets the defenderCloudBlockLevel property value. Possible values of Cloud Block Level
        Args:
            value: Value to set for the defender_cloud_block_level property.
        """
        self._defender_cloud_block_level = value
    
    @property
    def defender_days_before_deleting_quarantined_malware(self,) -> Optional[int]:
        """
        Gets the defenderDaysBeforeDeletingQuarantinedMalware property value. Number of days before deleting quarantined malware. Valid values 0 to 90
        Returns: Optional[int]
        """
        return self._defender_days_before_deleting_quarantined_malware
    
    @defender_days_before_deleting_quarantined_malware.setter
    def defender_days_before_deleting_quarantined_malware(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderDaysBeforeDeletingQuarantinedMalware property value. Number of days before deleting quarantined malware. Valid values 0 to 90
        Args:
            value: Value to set for the defender_days_before_deleting_quarantined_malware property.
        """
        self._defender_days_before_deleting_quarantined_malware = value
    
    @property
    def defender_detected_malware_actions(self,) -> Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions]:
        """
        Gets the defenderDetectedMalwareActions property value. Gets or sets Defender’s actions to take on detected Malware per threat level.
        Returns: Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions]
        """
        return self._defender_detected_malware_actions
    
    @defender_detected_malware_actions.setter
    def defender_detected_malware_actions(self,value: Optional[defender_detected_malware_actions.DefenderDetectedMalwareActions] = None) -> None:
        """
        Sets the defenderDetectedMalwareActions property value. Gets or sets Defender’s actions to take on detected Malware per threat level.
        Args:
            value: Value to set for the defender_detected_malware_actions property.
        """
        self._defender_detected_malware_actions = value
    
    @property
    def defender_file_extensions_to_exclude(self,) -> Optional[List[str]]:
        """
        Gets the defenderFileExtensionsToExclude property value. File extensions to exclude from scans and real time protection.
        Returns: Optional[List[str]]
        """
        return self._defender_file_extensions_to_exclude
    
    @defender_file_extensions_to_exclude.setter
    def defender_file_extensions_to_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderFileExtensionsToExclude property value. File extensions to exclude from scans and real time protection.
        Args:
            value: Value to set for the defender_file_extensions_to_exclude property.
        """
        self._defender_file_extensions_to_exclude = value
    
    @property
    def defender_files_and_folders_to_exclude(self,) -> Optional[List[str]]:
        """
        Gets the defenderFilesAndFoldersToExclude property value. Files and folder to exclude from scans and real time protection.
        Returns: Optional[List[str]]
        """
        return self._defender_files_and_folders_to_exclude
    
    @defender_files_and_folders_to_exclude.setter
    def defender_files_and_folders_to_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderFilesAndFoldersToExclude property value. Files and folder to exclude from scans and real time protection.
        Args:
            value: Value to set for the defender_files_and_folders_to_exclude property.
        """
        self._defender_files_and_folders_to_exclude = value
    
    @property
    def defender_monitor_file_activity(self,) -> Optional[defender_monitor_file_activity.DefenderMonitorFileActivity]:
        """
        Gets the defenderMonitorFileActivity property value. Possible values for monitoring file activity.
        Returns: Optional[defender_monitor_file_activity.DefenderMonitorFileActivity]
        """
        return self._defender_monitor_file_activity
    
    @defender_monitor_file_activity.setter
    def defender_monitor_file_activity(self,value: Optional[defender_monitor_file_activity.DefenderMonitorFileActivity] = None) -> None:
        """
        Sets the defenderMonitorFileActivity property value. Possible values for monitoring file activity.
        Args:
            value: Value to set for the defender_monitor_file_activity property.
        """
        self._defender_monitor_file_activity = value
    
    @property
    def defender_processes_to_exclude(self,) -> Optional[List[str]]:
        """
        Gets the defenderProcessesToExclude property value. Processes to exclude from scans and real time protection.
        Returns: Optional[List[str]]
        """
        return self._defender_processes_to_exclude
    
    @defender_processes_to_exclude.setter
    def defender_processes_to_exclude(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderProcessesToExclude property value. Processes to exclude from scans and real time protection.
        Args:
            value: Value to set for the defender_processes_to_exclude property.
        """
        self._defender_processes_to_exclude = value
    
    @property
    def defender_prompt_for_sample_submission(self,) -> Optional[defender_prompt_for_sample_submission.DefenderPromptForSampleSubmission]:
        """
        Gets the defenderPromptForSampleSubmission property value. Possible values for prompting user for samples submission.
        Returns: Optional[defender_prompt_for_sample_submission.DefenderPromptForSampleSubmission]
        """
        return self._defender_prompt_for_sample_submission
    
    @defender_prompt_for_sample_submission.setter
    def defender_prompt_for_sample_submission(self,value: Optional[defender_prompt_for_sample_submission.DefenderPromptForSampleSubmission] = None) -> None:
        """
        Sets the defenderPromptForSampleSubmission property value. Possible values for prompting user for samples submission.
        Args:
            value: Value to set for the defender_prompt_for_sample_submission property.
        """
        self._defender_prompt_for_sample_submission = value
    
    @property
    def defender_require_behavior_monitoring(self,) -> Optional[bool]:
        """
        Gets the defenderRequireBehaviorMonitoring property value. Indicates whether or not to require behavior monitoring.
        Returns: Optional[bool]
        """
        return self._defender_require_behavior_monitoring
    
    @defender_require_behavior_monitoring.setter
    def defender_require_behavior_monitoring(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderRequireBehaviorMonitoring property value. Indicates whether or not to require behavior monitoring.
        Args:
            value: Value to set for the defender_require_behavior_monitoring property.
        """
        self._defender_require_behavior_monitoring = value
    
    @property
    def defender_require_cloud_protection(self,) -> Optional[bool]:
        """
        Gets the defenderRequireCloudProtection property value. Indicates whether or not to require cloud protection.
        Returns: Optional[bool]
        """
        return self._defender_require_cloud_protection
    
    @defender_require_cloud_protection.setter
    def defender_require_cloud_protection(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderRequireCloudProtection property value. Indicates whether or not to require cloud protection.
        Args:
            value: Value to set for the defender_require_cloud_protection property.
        """
        self._defender_require_cloud_protection = value
    
    @property
    def defender_require_network_inspection_system(self,) -> Optional[bool]:
        """
        Gets the defenderRequireNetworkInspectionSystem property value. Indicates whether or not to require network inspection system.
        Returns: Optional[bool]
        """
        return self._defender_require_network_inspection_system
    
    @defender_require_network_inspection_system.setter
    def defender_require_network_inspection_system(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderRequireNetworkInspectionSystem property value. Indicates whether or not to require network inspection system.
        Args:
            value: Value to set for the defender_require_network_inspection_system property.
        """
        self._defender_require_network_inspection_system = value
    
    @property
    def defender_require_real_time_monitoring(self,) -> Optional[bool]:
        """
        Gets the defenderRequireRealTimeMonitoring property value. Indicates whether or not to require real time monitoring.
        Returns: Optional[bool]
        """
        return self._defender_require_real_time_monitoring
    
    @defender_require_real_time_monitoring.setter
    def defender_require_real_time_monitoring(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderRequireRealTimeMonitoring property value. Indicates whether or not to require real time monitoring.
        Args:
            value: Value to set for the defender_require_real_time_monitoring property.
        """
        self._defender_require_real_time_monitoring = value
    
    @property
    def defender_scan_archive_files(self,) -> Optional[bool]:
        """
        Gets the defenderScanArchiveFiles property value. Indicates whether or not to scan archive files.
        Returns: Optional[bool]
        """
        return self._defender_scan_archive_files
    
    @defender_scan_archive_files.setter
    def defender_scan_archive_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanArchiveFiles property value. Indicates whether or not to scan archive files.
        Args:
            value: Value to set for the defender_scan_archive_files property.
        """
        self._defender_scan_archive_files = value
    
    @property
    def defender_scan_downloads(self,) -> Optional[bool]:
        """
        Gets the defenderScanDownloads property value. Indicates whether or not to scan downloads.
        Returns: Optional[bool]
        """
        return self._defender_scan_downloads
    
    @defender_scan_downloads.setter
    def defender_scan_downloads(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanDownloads property value. Indicates whether or not to scan downloads.
        Args:
            value: Value to set for the defender_scan_downloads property.
        """
        self._defender_scan_downloads = value
    
    @property
    def defender_scan_incoming_mail(self,) -> Optional[bool]:
        """
        Gets the defenderScanIncomingMail property value. Indicates whether or not to scan incoming mail messages.
        Returns: Optional[bool]
        """
        return self._defender_scan_incoming_mail
    
    @defender_scan_incoming_mail.setter
    def defender_scan_incoming_mail(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanIncomingMail property value. Indicates whether or not to scan incoming mail messages.
        Args:
            value: Value to set for the defender_scan_incoming_mail property.
        """
        self._defender_scan_incoming_mail = value
    
    @property
    def defender_scan_mapped_network_drives_during_full_scan(self,) -> Optional[bool]:
        """
        Gets the defenderScanMappedNetworkDrivesDuringFullScan property value. Indicates whether or not to scan mapped network drives during full scan.
        Returns: Optional[bool]
        """
        return self._defender_scan_mapped_network_drives_during_full_scan
    
    @defender_scan_mapped_network_drives_during_full_scan.setter
    def defender_scan_mapped_network_drives_during_full_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanMappedNetworkDrivesDuringFullScan property value. Indicates whether or not to scan mapped network drives during full scan.
        Args:
            value: Value to set for the defender_scan_mapped_network_drives_during_full_scan property.
        """
        self._defender_scan_mapped_network_drives_during_full_scan = value
    
    @property
    def defender_scan_max_cpu(self,) -> Optional[int]:
        """
        Gets the defenderScanMaxCpu property value. Max CPU usage percentage during scan. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._defender_scan_max_cpu
    
    @defender_scan_max_cpu.setter
    def defender_scan_max_cpu(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderScanMaxCpu property value. Max CPU usage percentage during scan. Valid values 0 to 100
        Args:
            value: Value to set for the defender_scan_max_cpu property.
        """
        self._defender_scan_max_cpu = value
    
    @property
    def defender_scan_network_files(self,) -> Optional[bool]:
        """
        Gets the defenderScanNetworkFiles property value. Indicates whether or not to scan files opened from a network folder.
        Returns: Optional[bool]
        """
        return self._defender_scan_network_files
    
    @defender_scan_network_files.setter
    def defender_scan_network_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanNetworkFiles property value. Indicates whether or not to scan files opened from a network folder.
        Args:
            value: Value to set for the defender_scan_network_files property.
        """
        self._defender_scan_network_files = value
    
    @property
    def defender_scan_removable_drives_during_full_scan(self,) -> Optional[bool]:
        """
        Gets the defenderScanRemovableDrivesDuringFullScan property value. Indicates whether or not to scan removable drives during full scan.
        Returns: Optional[bool]
        """
        return self._defender_scan_removable_drives_during_full_scan
    
    @defender_scan_removable_drives_during_full_scan.setter
    def defender_scan_removable_drives_during_full_scan(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanRemovableDrivesDuringFullScan property value. Indicates whether or not to scan removable drives during full scan.
        Args:
            value: Value to set for the defender_scan_removable_drives_during_full_scan property.
        """
        self._defender_scan_removable_drives_during_full_scan = value
    
    @property
    def defender_scan_scripts_loaded_in_internet_explorer(self,) -> Optional[bool]:
        """
        Gets the defenderScanScriptsLoadedInInternetExplorer property value. Indicates whether or not to scan scripts loaded in Internet Explorer browser.
        Returns: Optional[bool]
        """
        return self._defender_scan_scripts_loaded_in_internet_explorer
    
    @defender_scan_scripts_loaded_in_internet_explorer.setter
    def defender_scan_scripts_loaded_in_internet_explorer(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderScanScriptsLoadedInInternetExplorer property value. Indicates whether or not to scan scripts loaded in Internet Explorer browser.
        Args:
            value: Value to set for the defender_scan_scripts_loaded_in_internet_explorer property.
        """
        self._defender_scan_scripts_loaded_in_internet_explorer = value
    
    @property
    def defender_scan_type(self,) -> Optional[defender_scan_type.DefenderScanType]:
        """
        Gets the defenderScanType property value. Possible values for system scan type.
        Returns: Optional[defender_scan_type.DefenderScanType]
        """
        return self._defender_scan_type
    
    @defender_scan_type.setter
    def defender_scan_type(self,value: Optional[defender_scan_type.DefenderScanType] = None) -> None:
        """
        Sets the defenderScanType property value. Possible values for system scan type.
        Args:
            value: Value to set for the defender_scan_type property.
        """
        self._defender_scan_type = value
    
    @property
    def defender_scheduled_quick_scan_time(self,) -> Optional[time]:
        """
        Gets the defenderScheduledQuickScanTime property value. The time to perform a daily quick scan.
        Returns: Optional[time]
        """
        return self._defender_scheduled_quick_scan_time
    
    @defender_scheduled_quick_scan_time.setter
    def defender_scheduled_quick_scan_time(self,value: Optional[time] = None) -> None:
        """
        Sets the defenderScheduledQuickScanTime property value. The time to perform a daily quick scan.
        Args:
            value: Value to set for the defender_scheduled_quick_scan_time property.
        """
        self._defender_scheduled_quick_scan_time = value
    
    @property
    def defender_scheduled_scan_time(self,) -> Optional[time]:
        """
        Gets the defenderScheduledScanTime property value. The defender time for the system scan.
        Returns: Optional[time]
        """
        return self._defender_scheduled_scan_time
    
    @defender_scheduled_scan_time.setter
    def defender_scheduled_scan_time(self,value: Optional[time] = None) -> None:
        """
        Sets the defenderScheduledScanTime property value. The defender time for the system scan.
        Args:
            value: Value to set for the defender_scheduled_scan_time property.
        """
        self._defender_scheduled_scan_time = value
    
    @property
    def defender_signature_update_interval_in_hours(self,) -> Optional[int]:
        """
        Gets the defenderSignatureUpdateIntervalInHours property value. The signature update interval in hours. Specify 0 not to check. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._defender_signature_update_interval_in_hours
    
    @defender_signature_update_interval_in_hours.setter
    def defender_signature_update_interval_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the defenderSignatureUpdateIntervalInHours property value. The signature update interval in hours. Specify 0 not to check. Valid values 0 to 24
        Args:
            value: Value to set for the defender_signature_update_interval_in_hours property.
        """
        self._defender_signature_update_interval_in_hours = value
    
    @property
    def defender_system_scan_schedule(self,) -> Optional[weekly_schedule.WeeklySchedule]:
        """
        Gets the defenderSystemScanSchedule property value. Possible values for a weekly schedule.
        Returns: Optional[weekly_schedule.WeeklySchedule]
        """
        return self._defender_system_scan_schedule
    
    @defender_system_scan_schedule.setter
    def defender_system_scan_schedule(self,value: Optional[weekly_schedule.WeeklySchedule] = None) -> None:
        """
        Sets the defenderSystemScanSchedule property value. Possible values for a weekly schedule.
        Args:
            value: Value to set for the defender_system_scan_schedule property.
        """
        self._defender_system_scan_schedule = value
    
    @property
    def developer_unlock_setting(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the developerUnlockSetting property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._developer_unlock_setting
    
    @developer_unlock_setting.setter
    def developer_unlock_setting(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the developerUnlockSetting property value. State Management Setting.
        Args:
            value: Value to set for the developer_unlock_setting property.
        """
        self._developer_unlock_setting = value
    
    @property
    def device_management_block_factory_reset_on_mobile(self,) -> Optional[bool]:
        """
        Gets the deviceManagementBlockFactoryResetOnMobile property value. Indicates whether or not to Block the user from resetting their phone.
        Returns: Optional[bool]
        """
        return self._device_management_block_factory_reset_on_mobile
    
    @device_management_block_factory_reset_on_mobile.setter
    def device_management_block_factory_reset_on_mobile(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceManagementBlockFactoryResetOnMobile property value. Indicates whether or not to Block the user from resetting their phone.
        Args:
            value: Value to set for the device_management_block_factory_reset_on_mobile property.
        """
        self._device_management_block_factory_reset_on_mobile = value
    
    @property
    def device_management_block_manual_unenroll(self,) -> Optional[bool]:
        """
        Gets the deviceManagementBlockManualUnenroll property value. Indicates whether or not to Block the user from doing manual un-enrollment from device management.
        Returns: Optional[bool]
        """
        return self._device_management_block_manual_unenroll
    
    @device_management_block_manual_unenroll.setter
    def device_management_block_manual_unenroll(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceManagementBlockManualUnenroll property value. Indicates whether or not to Block the user from doing manual un-enrollment from device management.
        Args:
            value: Value to set for the device_management_block_manual_unenroll property.
        """
        self._device_management_block_manual_unenroll = value
    
    @property
    def diagnostics_data_submission_mode(self,) -> Optional[diagnostic_data_submission_mode.DiagnosticDataSubmissionMode]:
        """
        Gets the diagnosticsDataSubmissionMode property value. Allow the device to send diagnostic and usage telemetry data, such as Watson.
        Returns: Optional[diagnostic_data_submission_mode.DiagnosticDataSubmissionMode]
        """
        return self._diagnostics_data_submission_mode
    
    @diagnostics_data_submission_mode.setter
    def diagnostics_data_submission_mode(self,value: Optional[diagnostic_data_submission_mode.DiagnosticDataSubmissionMode] = None) -> None:
        """
        Sets the diagnosticsDataSubmissionMode property value. Allow the device to send diagnostic and usage telemetry data, such as Watson.
        Args:
            value: Value to set for the diagnostics_data_submission_mode property.
        """
        self._diagnostics_data_submission_mode = value
    
    @property
    def edge_allow_start_pages_modification(self,) -> Optional[bool]:
        """
        Gets the edgeAllowStartPagesModification property value. Allow users to change Start pages on Edge. Use the EdgeHomepageUrls to specify the Start pages that the user would see by default when they open Edge.
        Returns: Optional[bool]
        """
        return self._edge_allow_start_pages_modification
    
    @edge_allow_start_pages_modification.setter
    def edge_allow_start_pages_modification(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeAllowStartPagesModification property value. Allow users to change Start pages on Edge. Use the EdgeHomepageUrls to specify the Start pages that the user would see by default when they open Edge.
        Args:
            value: Value to set for the edge_allow_start_pages_modification property.
        """
        self._edge_allow_start_pages_modification = value
    
    @property
    def edge_block_access_to_about_flags(self,) -> Optional[bool]:
        """
        Gets the edgeBlockAccessToAboutFlags property value. Indicates whether or not to prevent access to about flags on Edge browser.
        Returns: Optional[bool]
        """
        return self._edge_block_access_to_about_flags
    
    @edge_block_access_to_about_flags.setter
    def edge_block_access_to_about_flags(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockAccessToAboutFlags property value. Indicates whether or not to prevent access to about flags on Edge browser.
        Args:
            value: Value to set for the edge_block_access_to_about_flags property.
        """
        self._edge_block_access_to_about_flags = value
    
    @property
    def edge_block_address_bar_dropdown(self,) -> Optional[bool]:
        """
        Gets the edgeBlockAddressBarDropdown property value. Block the address bar dropdown functionality in Microsoft Edge. Disable this settings to minimize network connections from Microsoft Edge to Microsoft services.
        Returns: Optional[bool]
        """
        return self._edge_block_address_bar_dropdown
    
    @edge_block_address_bar_dropdown.setter
    def edge_block_address_bar_dropdown(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockAddressBarDropdown property value. Block the address bar dropdown functionality in Microsoft Edge. Disable this settings to minimize network connections from Microsoft Edge to Microsoft services.
        Args:
            value: Value to set for the edge_block_address_bar_dropdown property.
        """
        self._edge_block_address_bar_dropdown = value
    
    @property
    def edge_block_autofill(self,) -> Optional[bool]:
        """
        Gets the edgeBlockAutofill property value. Indicates whether or not to block auto fill.
        Returns: Optional[bool]
        """
        return self._edge_block_autofill
    
    @edge_block_autofill.setter
    def edge_block_autofill(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockAutofill property value. Indicates whether or not to block auto fill.
        Args:
            value: Value to set for the edge_block_autofill property.
        """
        self._edge_block_autofill = value
    
    @property
    def edge_block_compatibility_list(self,) -> Optional[bool]:
        """
        Gets the edgeBlockCompatibilityList property value. Block Microsoft compatibility list in Microsoft Edge. This list from Microsoft helps Edge properly display sites with known compatibility issues.
        Returns: Optional[bool]
        """
        return self._edge_block_compatibility_list
    
    @edge_block_compatibility_list.setter
    def edge_block_compatibility_list(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockCompatibilityList property value. Block Microsoft compatibility list in Microsoft Edge. This list from Microsoft helps Edge properly display sites with known compatibility issues.
        Args:
            value: Value to set for the edge_block_compatibility_list property.
        """
        self._edge_block_compatibility_list = value
    
    @property
    def edge_block_developer_tools(self,) -> Optional[bool]:
        """
        Gets the edgeBlockDeveloperTools property value. Indicates whether or not to block developer tools in the Edge browser.
        Returns: Optional[bool]
        """
        return self._edge_block_developer_tools
    
    @edge_block_developer_tools.setter
    def edge_block_developer_tools(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockDeveloperTools property value. Indicates whether or not to block developer tools in the Edge browser.
        Args:
            value: Value to set for the edge_block_developer_tools property.
        """
        self._edge_block_developer_tools = value
    
    @property
    def edge_block_extensions(self,) -> Optional[bool]:
        """
        Gets the edgeBlockExtensions property value. Indicates whether or not to block extensions in the Edge browser.
        Returns: Optional[bool]
        """
        return self._edge_block_extensions
    
    @edge_block_extensions.setter
    def edge_block_extensions(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockExtensions property value. Indicates whether or not to block extensions in the Edge browser.
        Args:
            value: Value to set for the edge_block_extensions property.
        """
        self._edge_block_extensions = value
    
    @property
    def edge_block_in_private_browsing(self,) -> Optional[bool]:
        """
        Gets the edgeBlockInPrivateBrowsing property value. Indicates whether or not to block InPrivate browsing on corporate networks, in the Edge browser.
        Returns: Optional[bool]
        """
        return self._edge_block_in_private_browsing
    
    @edge_block_in_private_browsing.setter
    def edge_block_in_private_browsing(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockInPrivateBrowsing property value. Indicates whether or not to block InPrivate browsing on corporate networks, in the Edge browser.
        Args:
            value: Value to set for the edge_block_in_private_browsing property.
        """
        self._edge_block_in_private_browsing = value
    
    @property
    def edge_block_java_script(self,) -> Optional[bool]:
        """
        Gets the edgeBlockJavaScript property value. Indicates whether or not to Block the user from using JavaScript.
        Returns: Optional[bool]
        """
        return self._edge_block_java_script
    
    @edge_block_java_script.setter
    def edge_block_java_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockJavaScript property value. Indicates whether or not to Block the user from using JavaScript.
        Args:
            value: Value to set for the edge_block_java_script property.
        """
        self._edge_block_java_script = value
    
    @property
    def edge_block_live_tile_data_collection(self,) -> Optional[bool]:
        """
        Gets the edgeBlockLiveTileDataCollection property value. Block the collection of information by Microsoft for live tile creation when users pin a site to Start from Microsoft Edge.
        Returns: Optional[bool]
        """
        return self._edge_block_live_tile_data_collection
    
    @edge_block_live_tile_data_collection.setter
    def edge_block_live_tile_data_collection(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockLiveTileDataCollection property value. Block the collection of information by Microsoft for live tile creation when users pin a site to Start from Microsoft Edge.
        Args:
            value: Value to set for the edge_block_live_tile_data_collection property.
        """
        self._edge_block_live_tile_data_collection = value
    
    @property
    def edge_block_password_manager(self,) -> Optional[bool]:
        """
        Gets the edgeBlockPasswordManager property value. Indicates whether or not to Block password manager.
        Returns: Optional[bool]
        """
        return self._edge_block_password_manager
    
    @edge_block_password_manager.setter
    def edge_block_password_manager(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockPasswordManager property value. Indicates whether or not to Block password manager.
        Args:
            value: Value to set for the edge_block_password_manager property.
        """
        self._edge_block_password_manager = value
    
    @property
    def edge_block_popups(self,) -> Optional[bool]:
        """
        Gets the edgeBlockPopups property value. Indicates whether or not to block popups.
        Returns: Optional[bool]
        """
        return self._edge_block_popups
    
    @edge_block_popups.setter
    def edge_block_popups(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockPopups property value. Indicates whether or not to block popups.
        Args:
            value: Value to set for the edge_block_popups property.
        """
        self._edge_block_popups = value
    
    @property
    def edge_block_search_suggestions(self,) -> Optional[bool]:
        """
        Gets the edgeBlockSearchSuggestions property value. Indicates whether or not to block the user from using the search suggestions in the address bar.
        Returns: Optional[bool]
        """
        return self._edge_block_search_suggestions
    
    @edge_block_search_suggestions.setter
    def edge_block_search_suggestions(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockSearchSuggestions property value. Indicates whether or not to block the user from using the search suggestions in the address bar.
        Args:
            value: Value to set for the edge_block_search_suggestions property.
        """
        self._edge_block_search_suggestions = value
    
    @property
    def edge_block_sending_do_not_track_header(self,) -> Optional[bool]:
        """
        Gets the edgeBlockSendingDoNotTrackHeader property value. Indicates whether or not to Block the user from sending the do not track header.
        Returns: Optional[bool]
        """
        return self._edge_block_sending_do_not_track_header
    
    @edge_block_sending_do_not_track_header.setter
    def edge_block_sending_do_not_track_header(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockSendingDoNotTrackHeader property value. Indicates whether or not to Block the user from sending the do not track header.
        Args:
            value: Value to set for the edge_block_sending_do_not_track_header property.
        """
        self._edge_block_sending_do_not_track_header = value
    
    @property
    def edge_block_sending_intranet_traffic_to_internet_explorer(self,) -> Optional[bool]:
        """
        Gets the edgeBlockSendingIntranetTrafficToInternetExplorer property value. Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer. Note: the name of this property is misleading; the property is obsolete, use EdgeSendIntranetTrafficToInternetExplorer instead.
        Returns: Optional[bool]
        """
        return self._edge_block_sending_intranet_traffic_to_internet_explorer
    
    @edge_block_sending_intranet_traffic_to_internet_explorer.setter
    def edge_block_sending_intranet_traffic_to_internet_explorer(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlockSendingIntranetTrafficToInternetExplorer property value. Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer. Note: the name of this property is misleading; the property is obsolete, use EdgeSendIntranetTrafficToInternetExplorer instead.
        Args:
            value: Value to set for the edge_block_sending_intranet_traffic_to_internet_explorer property.
        """
        self._edge_block_sending_intranet_traffic_to_internet_explorer = value
    
    @property
    def edge_blocked(self,) -> Optional[bool]:
        """
        Gets the edgeBlocked property value. Indicates whether or not to Block the user from using the Edge browser.
        Returns: Optional[bool]
        """
        return self._edge_blocked
    
    @edge_blocked.setter
    def edge_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeBlocked property value. Indicates whether or not to Block the user from using the Edge browser.
        Args:
            value: Value to set for the edge_blocked property.
        """
        self._edge_blocked = value
    
    @property
    def edge_clear_browsing_data_on_exit(self,) -> Optional[bool]:
        """
        Gets the edgeClearBrowsingDataOnExit property value. Clear browsing data on exiting Microsoft Edge.
        Returns: Optional[bool]
        """
        return self._edge_clear_browsing_data_on_exit
    
    @edge_clear_browsing_data_on_exit.setter
    def edge_clear_browsing_data_on_exit(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeClearBrowsingDataOnExit property value. Clear browsing data on exiting Microsoft Edge.
        Args:
            value: Value to set for the edge_clear_browsing_data_on_exit property.
        """
        self._edge_clear_browsing_data_on_exit = value
    
    @property
    def edge_cookie_policy(self,) -> Optional[edge_cookie_policy.EdgeCookiePolicy]:
        """
        Gets the edgeCookiePolicy property value. Possible values to specify which cookies are allowed in Microsoft Edge.
        Returns: Optional[edge_cookie_policy.EdgeCookiePolicy]
        """
        return self._edge_cookie_policy
    
    @edge_cookie_policy.setter
    def edge_cookie_policy(self,value: Optional[edge_cookie_policy.EdgeCookiePolicy] = None) -> None:
        """
        Sets the edgeCookiePolicy property value. Possible values to specify which cookies are allowed in Microsoft Edge.
        Args:
            value: Value to set for the edge_cookie_policy property.
        """
        self._edge_cookie_policy = value
    
    @property
    def edge_disable_first_run_page(self,) -> Optional[bool]:
        """
        Gets the edgeDisableFirstRunPage property value. Block the Microsoft web page that opens on the first use of Microsoft Edge. This policy allows enterprises, like those enrolled in zero emissions configurations, to block this page.
        Returns: Optional[bool]
        """
        return self._edge_disable_first_run_page
    
    @edge_disable_first_run_page.setter
    def edge_disable_first_run_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeDisableFirstRunPage property value. Block the Microsoft web page that opens on the first use of Microsoft Edge. This policy allows enterprises, like those enrolled in zero emissions configurations, to block this page.
        Args:
            value: Value to set for the edge_disable_first_run_page property.
        """
        self._edge_disable_first_run_page = value
    
    @property
    def edge_enterprise_mode_site_list_location(self,) -> Optional[str]:
        """
        Gets the edgeEnterpriseModeSiteListLocation property value. Indicates the enterprise mode site list location. Could be a local file, local network or http location.
        Returns: Optional[str]
        """
        return self._edge_enterprise_mode_site_list_location
    
    @edge_enterprise_mode_site_list_location.setter
    def edge_enterprise_mode_site_list_location(self,value: Optional[str] = None) -> None:
        """
        Sets the edgeEnterpriseModeSiteListLocation property value. Indicates the enterprise mode site list location. Could be a local file, local network or http location.
        Args:
            value: Value to set for the edge_enterprise_mode_site_list_location property.
        """
        self._edge_enterprise_mode_site_list_location = value
    
    @property
    def edge_first_run_url(self,) -> Optional[str]:
        """
        Gets the edgeFirstRunUrl property value. The first run URL for when Edge browser is opened for the first time.
        Returns: Optional[str]
        """
        return self._edge_first_run_url
    
    @edge_first_run_url.setter
    def edge_first_run_url(self,value: Optional[str] = None) -> None:
        """
        Sets the edgeFirstRunUrl property value. The first run URL for when Edge browser is opened for the first time.
        Args:
            value: Value to set for the edge_first_run_url property.
        """
        self._edge_first_run_url = value
    
    @property
    def edge_homepage_urls(self,) -> Optional[List[str]]:
        """
        Gets the edgeHomepageUrls property value. The list of URLs for homepages shodwn on MDM-enrolled devices on Edge browser.
        Returns: Optional[List[str]]
        """
        return self._edge_homepage_urls
    
    @edge_homepage_urls.setter
    def edge_homepage_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the edgeHomepageUrls property value. The list of URLs for homepages shodwn on MDM-enrolled devices on Edge browser.
        Args:
            value: Value to set for the edge_homepage_urls property.
        """
        self._edge_homepage_urls = value
    
    @property
    def edge_require_smart_screen(self,) -> Optional[bool]:
        """
        Gets the edgeRequireSmartScreen property value. Indicates whether or not to Require the user to use the smart screen filter.
        Returns: Optional[bool]
        """
        return self._edge_require_smart_screen
    
    @edge_require_smart_screen.setter
    def edge_require_smart_screen(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeRequireSmartScreen property value. Indicates whether or not to Require the user to use the smart screen filter.
        Args:
            value: Value to set for the edge_require_smart_screen property.
        """
        self._edge_require_smart_screen = value
    
    @property
    def edge_search_engine(self,) -> Optional[edge_search_engine_base.EdgeSearchEngineBase]:
        """
        Gets the edgeSearchEngine property value. Allows IT admins to set a default search engine for MDM-Controlled devices. Users can override this and change their default search engine provided the AllowSearchEngineCustomization policy is not set.
        Returns: Optional[edge_search_engine_base.EdgeSearchEngineBase]
        """
        return self._edge_search_engine
    
    @edge_search_engine.setter
    def edge_search_engine(self,value: Optional[edge_search_engine_base.EdgeSearchEngineBase] = None) -> None:
        """
        Sets the edgeSearchEngine property value. Allows IT admins to set a default search engine for MDM-Controlled devices. Users can override this and change their default search engine provided the AllowSearchEngineCustomization policy is not set.
        Args:
            value: Value to set for the edge_search_engine property.
        """
        self._edge_search_engine = value
    
    @property
    def edge_send_intranet_traffic_to_internet_explorer(self,) -> Optional[bool]:
        """
        Gets the edgeSendIntranetTrafficToInternetExplorer property value. Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer.
        Returns: Optional[bool]
        """
        return self._edge_send_intranet_traffic_to_internet_explorer
    
    @edge_send_intranet_traffic_to_internet_explorer.setter
    def edge_send_intranet_traffic_to_internet_explorer(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeSendIntranetTrafficToInternetExplorer property value. Indicates whether or not to switch the intranet traffic from Edge to Internet Explorer.
        Args:
            value: Value to set for the edge_send_intranet_traffic_to_internet_explorer property.
        """
        self._edge_send_intranet_traffic_to_internet_explorer = value
    
    @property
    def edge_sync_favorites_with_internet_explorer(self,) -> Optional[bool]:
        """
        Gets the edgeSyncFavoritesWithInternetExplorer property value. Enable favorites sync between Internet Explorer and Microsoft Edge. Additions, deletions, modifications and order changes to favorites are shared between browsers.
        Returns: Optional[bool]
        """
        return self._edge_sync_favorites_with_internet_explorer
    
    @edge_sync_favorites_with_internet_explorer.setter
    def edge_sync_favorites_with_internet_explorer(self,value: Optional[bool] = None) -> None:
        """
        Sets the edgeSyncFavoritesWithInternetExplorer property value. Enable favorites sync between Internet Explorer and Microsoft Edge. Additions, deletions, modifications and order changes to favorites are shared between browsers.
        Args:
            value: Value to set for the edge_sync_favorites_with_internet_explorer property.
        """
        self._edge_sync_favorites_with_internet_explorer = value
    
    @property
    def enterprise_cloud_print_discovery_end_point(self,) -> Optional[str]:
        """
        Gets the enterpriseCloudPrintDiscoveryEndPoint property value. Endpoint for discovering cloud printers.
        Returns: Optional[str]
        """
        return self._enterprise_cloud_print_discovery_end_point
    
    @enterprise_cloud_print_discovery_end_point.setter
    def enterprise_cloud_print_discovery_end_point(self,value: Optional[str] = None) -> None:
        """
        Sets the enterpriseCloudPrintDiscoveryEndPoint property value. Endpoint for discovering cloud printers.
        Args:
            value: Value to set for the enterprise_cloud_print_discovery_end_point property.
        """
        self._enterprise_cloud_print_discovery_end_point = value
    
    @property
    def enterprise_cloud_print_discovery_max_limit(self,) -> Optional[int]:
        """
        Gets the enterpriseCloudPrintDiscoveryMaxLimit property value. Maximum number of printers that should be queried from a discovery endpoint. This is a mobile only setting. Valid values 1 to 65535
        Returns: Optional[int]
        """
        return self._enterprise_cloud_print_discovery_max_limit
    
    @enterprise_cloud_print_discovery_max_limit.setter
    def enterprise_cloud_print_discovery_max_limit(self,value: Optional[int] = None) -> None:
        """
        Sets the enterpriseCloudPrintDiscoveryMaxLimit property value. Maximum number of printers that should be queried from a discovery endpoint. This is a mobile only setting. Valid values 1 to 65535
        Args:
            value: Value to set for the enterprise_cloud_print_discovery_max_limit property.
        """
        self._enterprise_cloud_print_discovery_max_limit = value
    
    @property
    def enterprise_cloud_print_mopria_discovery_resource_identifier(self,) -> Optional[str]:
        """
        Gets the enterpriseCloudPrintMopriaDiscoveryResourceIdentifier property value. OAuth resource URI for printer discovery service as configured in Azure portal.
        Returns: Optional[str]
        """
        return self._enterprise_cloud_print_mopria_discovery_resource_identifier
    
    @enterprise_cloud_print_mopria_discovery_resource_identifier.setter
    def enterprise_cloud_print_mopria_discovery_resource_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the enterpriseCloudPrintMopriaDiscoveryResourceIdentifier property value. OAuth resource URI for printer discovery service as configured in Azure portal.
        Args:
            value: Value to set for the enterprise_cloud_print_mopria_discovery_resource_identifier property.
        """
        self._enterprise_cloud_print_mopria_discovery_resource_identifier = value
    
    @property
    def enterprise_cloud_print_o_auth_authority(self,) -> Optional[str]:
        """
        Gets the enterpriseCloudPrintOAuthAuthority property value. Authentication endpoint for acquiring OAuth tokens.
        Returns: Optional[str]
        """
        return self._enterprise_cloud_print_o_auth_authority
    
    @enterprise_cloud_print_o_auth_authority.setter
    def enterprise_cloud_print_o_auth_authority(self,value: Optional[str] = None) -> None:
        """
        Sets the enterpriseCloudPrintOAuthAuthority property value. Authentication endpoint for acquiring OAuth tokens.
        Args:
            value: Value to set for the enterprise_cloud_print_o_auth_authority property.
        """
        self._enterprise_cloud_print_o_auth_authority = value
    
    @property
    def enterprise_cloud_print_o_auth_client_identifier(self,) -> Optional[str]:
        """
        Gets the enterpriseCloudPrintOAuthClientIdentifier property value. GUID of a client application authorized to retrieve OAuth tokens from the OAuth Authority.
        Returns: Optional[str]
        """
        return self._enterprise_cloud_print_o_auth_client_identifier
    
    @enterprise_cloud_print_o_auth_client_identifier.setter
    def enterprise_cloud_print_o_auth_client_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the enterpriseCloudPrintOAuthClientIdentifier property value. GUID of a client application authorized to retrieve OAuth tokens from the OAuth Authority.
        Args:
            value: Value to set for the enterprise_cloud_print_o_auth_client_identifier property.
        """
        self._enterprise_cloud_print_o_auth_client_identifier = value
    
    @property
    def enterprise_cloud_print_resource_identifier(self,) -> Optional[str]:
        """
        Gets the enterpriseCloudPrintResourceIdentifier property value. OAuth resource URI for print service as configured in the Azure portal.
        Returns: Optional[str]
        """
        return self._enterprise_cloud_print_resource_identifier
    
    @enterprise_cloud_print_resource_identifier.setter
    def enterprise_cloud_print_resource_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the enterpriseCloudPrintResourceIdentifier property value. OAuth resource URI for print service as configured in the Azure portal.
        Args:
            value: Value to set for the enterprise_cloud_print_resource_identifier property.
        """
        self._enterprise_cloud_print_resource_identifier = value
    
    @property
    def experience_block_device_discovery(self,) -> Optional[bool]:
        """
        Gets the experienceBlockDeviceDiscovery property value. Indicates whether or not to enable device discovery UX.
        Returns: Optional[bool]
        """
        return self._experience_block_device_discovery
    
    @experience_block_device_discovery.setter
    def experience_block_device_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the experienceBlockDeviceDiscovery property value. Indicates whether or not to enable device discovery UX.
        Args:
            value: Value to set for the experience_block_device_discovery property.
        """
        self._experience_block_device_discovery = value
    
    @property
    def experience_block_error_dialog_when_no_s_i_m(self,) -> Optional[bool]:
        """
        Gets the experienceBlockErrorDialogWhenNoSIM property value. Indicates whether or not to allow the error dialog from displaying if no SIM card is detected.
        Returns: Optional[bool]
        """
        return self._experience_block_error_dialog_when_no_s_i_m
    
    @experience_block_error_dialog_when_no_s_i_m.setter
    def experience_block_error_dialog_when_no_s_i_m(self,value: Optional[bool] = None) -> None:
        """
        Sets the experienceBlockErrorDialogWhenNoSIM property value. Indicates whether or not to allow the error dialog from displaying if no SIM card is detected.
        Args:
            value: Value to set for the experience_block_error_dialog_when_no_s_i_m property.
        """
        self._experience_block_error_dialog_when_no_s_i_m = value
    
    @property
    def experience_block_task_switcher(self,) -> Optional[bool]:
        """
        Gets the experienceBlockTaskSwitcher property value. Indicates whether or not to enable task switching on the device.
        Returns: Optional[bool]
        """
        return self._experience_block_task_switcher
    
    @experience_block_task_switcher.setter
    def experience_block_task_switcher(self,value: Optional[bool] = None) -> None:
        """
        Sets the experienceBlockTaskSwitcher property value. Indicates whether or not to enable task switching on the device.
        Args:
            value: Value to set for the experience_block_task_switcher property.
        """
        self._experience_block_task_switcher = value
    
    @property
    def game_dvr_blocked(self,) -> Optional[bool]:
        """
        Gets the gameDvrBlocked property value. Indicates whether or not to block DVR and broadcasting.
        Returns: Optional[bool]
        """
        return self._game_dvr_blocked
    
    @game_dvr_blocked.setter
    def game_dvr_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the gameDvrBlocked property value. Indicates whether or not to block DVR and broadcasting.
        Args:
            value: Value to set for the game_dvr_blocked property.
        """
        self._game_dvr_blocked = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import defender_cloud_block_level_type, defender_detected_malware_actions, defender_monitor_file_activity, defender_prompt_for_sample_submission, defender_scan_type, device_configuration, diagnostic_data_submission_mode, edge_cookie_policy, edge_search_engine_base, required_password_type, safe_search_filter_type, state_management_setting, visibility_setting, weekly_schedule, windows10_network_proxy_server, windows_spotlight_enablement_settings, windows_start_menu_app_list_visibility_type, windows_start_menu_mode_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accountsBlockAddingNonMicrosoftAccountEmail": lambda n : setattr(self, 'accounts_block_adding_non_microsoft_account_email', n.get_bool_value()),
            "antiTheftModeBlocked": lambda n : setattr(self, 'anti_theft_mode_blocked', n.get_bool_value()),
            "appsAllowTrustedAppsSideloading": lambda n : setattr(self, 'apps_allow_trusted_apps_sideloading', n.get_enum_value(state_management_setting.StateManagementSetting)),
            "appsBlockWindowsStoreOriginatedApps": lambda n : setattr(self, 'apps_block_windows_store_originated_apps', n.get_bool_value()),
            "bluetoothAllowedServices": lambda n : setattr(self, 'bluetooth_allowed_services', n.get_collection_of_primitive_values(str)),
            "bluetoothBlocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "bluetoothBlockAdvertising": lambda n : setattr(self, 'bluetooth_block_advertising', n.get_bool_value()),
            "bluetoothBlockDiscoverableMode": lambda n : setattr(self, 'bluetooth_block_discoverable_mode', n.get_bool_value()),
            "bluetoothBlockPrePairing": lambda n : setattr(self, 'bluetooth_block_pre_pairing', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellularBlockDataWhenRoaming": lambda n : setattr(self, 'cellular_block_data_when_roaming', n.get_bool_value()),
            "cellularBlockVpn": lambda n : setattr(self, 'cellular_block_vpn', n.get_bool_value()),
            "cellularBlockVpnWhenRoaming": lambda n : setattr(self, 'cellular_block_vpn_when_roaming', n.get_bool_value()),
            "certificatesBlockManualRootCertificateInstallation": lambda n : setattr(self, 'certificates_block_manual_root_certificate_installation', n.get_bool_value()),
            "connectedDevicesServiceBlocked": lambda n : setattr(self, 'connected_devices_service_blocked', n.get_bool_value()),
            "copyPasteBlocked": lambda n : setattr(self, 'copy_paste_blocked', n.get_bool_value()),
            "cortanaBlocked": lambda n : setattr(self, 'cortana_blocked', n.get_bool_value()),
            "defenderBlockEndUserAccess": lambda n : setattr(self, 'defender_block_end_user_access', n.get_bool_value()),
            "defenderCloudBlockLevel": lambda n : setattr(self, 'defender_cloud_block_level', n.get_enum_value(defender_cloud_block_level_type.DefenderCloudBlockLevelType)),
            "defenderDaysBeforeDeletingQuarantinedMalware": lambda n : setattr(self, 'defender_days_before_deleting_quarantined_malware', n.get_int_value()),
            "defenderDetectedMalwareActions": lambda n : setattr(self, 'defender_detected_malware_actions', n.get_object_value(defender_detected_malware_actions.DefenderDetectedMalwareActions)),
            "defenderFilesAndFoldersToExclude": lambda n : setattr(self, 'defender_files_and_folders_to_exclude', n.get_collection_of_primitive_values(str)),
            "defenderFileExtensionsToExclude": lambda n : setattr(self, 'defender_file_extensions_to_exclude', n.get_collection_of_primitive_values(str)),
            "defenderMonitorFileActivity": lambda n : setattr(self, 'defender_monitor_file_activity', n.get_enum_value(defender_monitor_file_activity.DefenderMonitorFileActivity)),
            "defenderProcessesToExclude": lambda n : setattr(self, 'defender_processes_to_exclude', n.get_collection_of_primitive_values(str)),
            "defenderPromptForSampleSubmission": lambda n : setattr(self, 'defender_prompt_for_sample_submission', n.get_enum_value(defender_prompt_for_sample_submission.DefenderPromptForSampleSubmission)),
            "defenderRequireBehaviorMonitoring": lambda n : setattr(self, 'defender_require_behavior_monitoring', n.get_bool_value()),
            "defenderRequireCloudProtection": lambda n : setattr(self, 'defender_require_cloud_protection', n.get_bool_value()),
            "defenderRequireNetworkInspectionSystem": lambda n : setattr(self, 'defender_require_network_inspection_system', n.get_bool_value()),
            "defenderRequireRealTimeMonitoring": lambda n : setattr(self, 'defender_require_real_time_monitoring', n.get_bool_value()),
            "defenderScanArchiveFiles": lambda n : setattr(self, 'defender_scan_archive_files', n.get_bool_value()),
            "defenderScanDownloads": lambda n : setattr(self, 'defender_scan_downloads', n.get_bool_value()),
            "defenderScanIncomingMail": lambda n : setattr(self, 'defender_scan_incoming_mail', n.get_bool_value()),
            "defenderScanMappedNetworkDrivesDuringFullScan": lambda n : setattr(self, 'defender_scan_mapped_network_drives_during_full_scan', n.get_bool_value()),
            "defenderScanMaxCpu": lambda n : setattr(self, 'defender_scan_max_cpu', n.get_int_value()),
            "defenderScanNetworkFiles": lambda n : setattr(self, 'defender_scan_network_files', n.get_bool_value()),
            "defenderScanRemovableDrivesDuringFullScan": lambda n : setattr(self, 'defender_scan_removable_drives_during_full_scan', n.get_bool_value()),
            "defenderScanScriptsLoadedInInternetExplorer": lambda n : setattr(self, 'defender_scan_scripts_loaded_in_internet_explorer', n.get_bool_value()),
            "defenderScanType": lambda n : setattr(self, 'defender_scan_type', n.get_enum_value(defender_scan_type.DefenderScanType)),
            "defenderScheduledQuickScanTime": lambda n : setattr(self, 'defender_scheduled_quick_scan_time', n.get_time_value()),
            "defenderScheduledScanTime": lambda n : setattr(self, 'defender_scheduled_scan_time', n.get_time_value()),
            "defenderSignatureUpdateIntervalInHours": lambda n : setattr(self, 'defender_signature_update_interval_in_hours', n.get_int_value()),
            "defenderSystemScanSchedule": lambda n : setattr(self, 'defender_system_scan_schedule', n.get_enum_value(weekly_schedule.WeeklySchedule)),
            "developerUnlockSetting": lambda n : setattr(self, 'developer_unlock_setting', n.get_enum_value(state_management_setting.StateManagementSetting)),
            "deviceManagementBlockFactoryResetOnMobile": lambda n : setattr(self, 'device_management_block_factory_reset_on_mobile', n.get_bool_value()),
            "deviceManagementBlockManualUnenroll": lambda n : setattr(self, 'device_management_block_manual_unenroll', n.get_bool_value()),
            "diagnosticsDataSubmissionMode": lambda n : setattr(self, 'diagnostics_data_submission_mode', n.get_enum_value(diagnostic_data_submission_mode.DiagnosticDataSubmissionMode)),
            "edgeAllowStartPagesModification": lambda n : setattr(self, 'edge_allow_start_pages_modification', n.get_bool_value()),
            "edgeBlocked": lambda n : setattr(self, 'edge_blocked', n.get_bool_value()),
            "edgeBlockAccessToAboutFlags": lambda n : setattr(self, 'edge_block_access_to_about_flags', n.get_bool_value()),
            "edgeBlockAddressBarDropdown": lambda n : setattr(self, 'edge_block_address_bar_dropdown', n.get_bool_value()),
            "edgeBlockAutofill": lambda n : setattr(self, 'edge_block_autofill', n.get_bool_value()),
            "edgeBlockCompatibilityList": lambda n : setattr(self, 'edge_block_compatibility_list', n.get_bool_value()),
            "edgeBlockDeveloperTools": lambda n : setattr(self, 'edge_block_developer_tools', n.get_bool_value()),
            "edgeBlockExtensions": lambda n : setattr(self, 'edge_block_extensions', n.get_bool_value()),
            "edgeBlockInPrivateBrowsing": lambda n : setattr(self, 'edge_block_in_private_browsing', n.get_bool_value()),
            "edgeBlockJavaScript": lambda n : setattr(self, 'edge_block_java_script', n.get_bool_value()),
            "edgeBlockLiveTileDataCollection": lambda n : setattr(self, 'edge_block_live_tile_data_collection', n.get_bool_value()),
            "edgeBlockPasswordManager": lambda n : setattr(self, 'edge_block_password_manager', n.get_bool_value()),
            "edgeBlockPopups": lambda n : setattr(self, 'edge_block_popups', n.get_bool_value()),
            "edgeBlockSearchSuggestions": lambda n : setattr(self, 'edge_block_search_suggestions', n.get_bool_value()),
            "edgeBlockSendingDoNotTrackHeader": lambda n : setattr(self, 'edge_block_sending_do_not_track_header', n.get_bool_value()),
            "edgeBlockSendingIntranetTrafficToInternetExplorer": lambda n : setattr(self, 'edge_block_sending_intranet_traffic_to_internet_explorer', n.get_bool_value()),
            "edgeClearBrowsingDataOnExit": lambda n : setattr(self, 'edge_clear_browsing_data_on_exit', n.get_bool_value()),
            "edgeCookiePolicy": lambda n : setattr(self, 'edge_cookie_policy', n.get_enum_value(edge_cookie_policy.EdgeCookiePolicy)),
            "edgeDisableFirstRunPage": lambda n : setattr(self, 'edge_disable_first_run_page', n.get_bool_value()),
            "edgeEnterpriseModeSiteListLocation": lambda n : setattr(self, 'edge_enterprise_mode_site_list_location', n.get_str_value()),
            "edgeFirstRunUrl": lambda n : setattr(self, 'edge_first_run_url', n.get_str_value()),
            "edgeHomepageUrls": lambda n : setattr(self, 'edge_homepage_urls', n.get_collection_of_primitive_values(str)),
            "edgeRequireSmartScreen": lambda n : setattr(self, 'edge_require_smart_screen', n.get_bool_value()),
            "edgeSearchEngine": lambda n : setattr(self, 'edge_search_engine', n.get_object_value(edge_search_engine_base.EdgeSearchEngineBase)),
            "edgeSendIntranetTrafficToInternetExplorer": lambda n : setattr(self, 'edge_send_intranet_traffic_to_internet_explorer', n.get_bool_value()),
            "edgeSyncFavoritesWithInternetExplorer": lambda n : setattr(self, 'edge_sync_favorites_with_internet_explorer', n.get_bool_value()),
            "enterpriseCloudPrintDiscoveryEndPoint": lambda n : setattr(self, 'enterprise_cloud_print_discovery_end_point', n.get_str_value()),
            "enterpriseCloudPrintDiscoveryMaxLimit": lambda n : setattr(self, 'enterprise_cloud_print_discovery_max_limit', n.get_int_value()),
            "enterpriseCloudPrintMopriaDiscoveryResourceIdentifier": lambda n : setattr(self, 'enterprise_cloud_print_mopria_discovery_resource_identifier', n.get_str_value()),
            "enterpriseCloudPrintOAuthAuthority": lambda n : setattr(self, 'enterprise_cloud_print_o_auth_authority', n.get_str_value()),
            "enterpriseCloudPrintOAuthClientIdentifier": lambda n : setattr(self, 'enterprise_cloud_print_o_auth_client_identifier', n.get_str_value()),
            "enterpriseCloudPrintResourceIdentifier": lambda n : setattr(self, 'enterprise_cloud_print_resource_identifier', n.get_str_value()),
            "experienceBlockDeviceDiscovery": lambda n : setattr(self, 'experience_block_device_discovery', n.get_bool_value()),
            "experienceBlockErrorDialogWhenNoSIM": lambda n : setattr(self, 'experience_block_error_dialog_when_no_s_i_m', n.get_bool_value()),
            "experienceBlockTaskSwitcher": lambda n : setattr(self, 'experience_block_task_switcher', n.get_bool_value()),
            "gameDvrBlocked": lambda n : setattr(self, 'game_dvr_blocked', n.get_bool_value()),
            "internetSharingBlocked": lambda n : setattr(self, 'internet_sharing_blocked', n.get_bool_value()),
            "locationServicesBlocked": lambda n : setattr(self, 'location_services_blocked', n.get_bool_value()),
            "lockScreenAllowTimeoutConfiguration": lambda n : setattr(self, 'lock_screen_allow_timeout_configuration', n.get_bool_value()),
            "lockScreenBlockActionCenterNotifications": lambda n : setattr(self, 'lock_screen_block_action_center_notifications', n.get_bool_value()),
            "lockScreenBlockCortana": lambda n : setattr(self, 'lock_screen_block_cortana', n.get_bool_value()),
            "lockScreenBlockToastNotifications": lambda n : setattr(self, 'lock_screen_block_toast_notifications', n.get_bool_value()),
            "lockScreenTimeoutInSeconds": lambda n : setattr(self, 'lock_screen_timeout_in_seconds', n.get_int_value()),
            "logonBlockFastUserSwitching": lambda n : setattr(self, 'logon_block_fast_user_switching', n.get_bool_value()),
            "microsoftAccountBlocked": lambda n : setattr(self, 'microsoft_account_blocked', n.get_bool_value()),
            "microsoftAccountBlockSettingsSync": lambda n : setattr(self, 'microsoft_account_block_settings_sync', n.get_bool_value()),
            "networkProxyApplySettingsDeviceWide": lambda n : setattr(self, 'network_proxy_apply_settings_device_wide', n.get_bool_value()),
            "networkProxyAutomaticConfigurationUrl": lambda n : setattr(self, 'network_proxy_automatic_configuration_url', n.get_str_value()),
            "networkProxyDisableAutoDetect": lambda n : setattr(self, 'network_proxy_disable_auto_detect', n.get_bool_value()),
            "networkProxyServer": lambda n : setattr(self, 'network_proxy_server', n.get_object_value(windows10_network_proxy_server.Windows10NetworkProxyServer)),
            "nfcBlocked": lambda n : setattr(self, 'nfc_blocked', n.get_bool_value()),
            "oneDriveDisableFileSync": lambda n : setattr(self, 'one_drive_disable_file_sync', n.get_bool_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "passwordRequireWhenResumeFromIdleState": lambda n : setattr(self, 'password_require_when_resume_from_idle_state', n.get_bool_value()),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "personalizationDesktopImageUrl": lambda n : setattr(self, 'personalization_desktop_image_url', n.get_str_value()),
            "personalizationLockScreenImageUrl": lambda n : setattr(self, 'personalization_lock_screen_image_url', n.get_str_value()),
            "privacyAdvertisingId": lambda n : setattr(self, 'privacy_advertising_id', n.get_enum_value(state_management_setting.StateManagementSetting)),
            "privacyAutoAcceptPairingAndConsentPrompts": lambda n : setattr(self, 'privacy_auto_accept_pairing_and_consent_prompts', n.get_bool_value()),
            "privacyBlockInputPersonalization": lambda n : setattr(self, 'privacy_block_input_personalization', n.get_bool_value()),
            "resetProtectionModeBlocked": lambda n : setattr(self, 'reset_protection_mode_blocked', n.get_bool_value()),
            "safeSearchFilter": lambda n : setattr(self, 'safe_search_filter', n.get_enum_value(safe_search_filter_type.SafeSearchFilterType)),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "searchBlockDiacritics": lambda n : setattr(self, 'search_block_diacritics', n.get_bool_value()),
            "searchDisableAutoLanguageDetection": lambda n : setattr(self, 'search_disable_auto_language_detection', n.get_bool_value()),
            "searchDisableIndexerBackoff": lambda n : setattr(self, 'search_disable_indexer_backoff', n.get_bool_value()),
            "searchDisableIndexingEncryptedItems": lambda n : setattr(self, 'search_disable_indexing_encrypted_items', n.get_bool_value()),
            "searchDisableIndexingRemovableDrive": lambda n : setattr(self, 'search_disable_indexing_removable_drive', n.get_bool_value()),
            "searchEnableAutomaticIndexSizeManangement": lambda n : setattr(self, 'search_enable_automatic_index_size_manangement', n.get_bool_value()),
            "searchEnableRemoteQueries": lambda n : setattr(self, 'search_enable_remote_queries', n.get_bool_value()),
            "settingsBlockAccountsPage": lambda n : setattr(self, 'settings_block_accounts_page', n.get_bool_value()),
            "settingsBlockAddProvisioningPackage": lambda n : setattr(self, 'settings_block_add_provisioning_package', n.get_bool_value()),
            "settingsBlockAppsPage": lambda n : setattr(self, 'settings_block_apps_page', n.get_bool_value()),
            "settingsBlockChangeLanguage": lambda n : setattr(self, 'settings_block_change_language', n.get_bool_value()),
            "settingsBlockChangePowerSleep": lambda n : setattr(self, 'settings_block_change_power_sleep', n.get_bool_value()),
            "settingsBlockChangeRegion": lambda n : setattr(self, 'settings_block_change_region', n.get_bool_value()),
            "settingsBlockChangeSystemTime": lambda n : setattr(self, 'settings_block_change_system_time', n.get_bool_value()),
            "settingsBlockDevicesPage": lambda n : setattr(self, 'settings_block_devices_page', n.get_bool_value()),
            "settingsBlockEaseOfAccessPage": lambda n : setattr(self, 'settings_block_ease_of_access_page', n.get_bool_value()),
            "settingsBlockEditDeviceName": lambda n : setattr(self, 'settings_block_edit_device_name', n.get_bool_value()),
            "settingsBlockGamingPage": lambda n : setattr(self, 'settings_block_gaming_page', n.get_bool_value()),
            "settingsBlockNetworkInternetPage": lambda n : setattr(self, 'settings_block_network_internet_page', n.get_bool_value()),
            "settingsBlockPersonalizationPage": lambda n : setattr(self, 'settings_block_personalization_page', n.get_bool_value()),
            "settingsBlockPrivacyPage": lambda n : setattr(self, 'settings_block_privacy_page', n.get_bool_value()),
            "settingsBlockRemoveProvisioningPackage": lambda n : setattr(self, 'settings_block_remove_provisioning_package', n.get_bool_value()),
            "settingsBlockSettingsApp": lambda n : setattr(self, 'settings_block_settings_app', n.get_bool_value()),
            "settingsBlockSystemPage": lambda n : setattr(self, 'settings_block_system_page', n.get_bool_value()),
            "settingsBlockTimeLanguagePage": lambda n : setattr(self, 'settings_block_time_language_page', n.get_bool_value()),
            "settingsBlockUpdateSecurityPage": lambda n : setattr(self, 'settings_block_update_security_page', n.get_bool_value()),
            "sharedUserAppDataAllowed": lambda n : setattr(self, 'shared_user_app_data_allowed', n.get_bool_value()),
            "smartScreenBlockPromptOverride": lambda n : setattr(self, 'smart_screen_block_prompt_override', n.get_bool_value()),
            "smartScreenBlockPromptOverrideForFiles": lambda n : setattr(self, 'smart_screen_block_prompt_override_for_files', n.get_bool_value()),
            "smartScreenEnableAppInstallControl": lambda n : setattr(self, 'smart_screen_enable_app_install_control', n.get_bool_value()),
            "startBlockUnpinningAppsFromTaskbar": lambda n : setattr(self, 'start_block_unpinning_apps_from_taskbar', n.get_bool_value()),
            "startMenuAppListVisibility": lambda n : setattr(self, 'start_menu_app_list_visibility', n.get_enum_value(windows_start_menu_app_list_visibility_type.WindowsStartMenuAppListVisibilityType)),
            "startMenuHideChangeAccountSettings": lambda n : setattr(self, 'start_menu_hide_change_account_settings', n.get_bool_value()),
            "startMenuHideFrequentlyUsedApps": lambda n : setattr(self, 'start_menu_hide_frequently_used_apps', n.get_bool_value()),
            "startMenuHideHibernate": lambda n : setattr(self, 'start_menu_hide_hibernate', n.get_bool_value()),
            "startMenuHideLock": lambda n : setattr(self, 'start_menu_hide_lock', n.get_bool_value()),
            "startMenuHidePowerButton": lambda n : setattr(self, 'start_menu_hide_power_button', n.get_bool_value()),
            "startMenuHideRecentlyAddedApps": lambda n : setattr(self, 'start_menu_hide_recently_added_apps', n.get_bool_value()),
            "startMenuHideRecentJumpLists": lambda n : setattr(self, 'start_menu_hide_recent_jump_lists', n.get_bool_value()),
            "startMenuHideRestartOptions": lambda n : setattr(self, 'start_menu_hide_restart_options', n.get_bool_value()),
            "startMenuHideShutDown": lambda n : setattr(self, 'start_menu_hide_shut_down', n.get_bool_value()),
            "startMenuHideSignOut": lambda n : setattr(self, 'start_menu_hide_sign_out', n.get_bool_value()),
            "startMenuHideSleep": lambda n : setattr(self, 'start_menu_hide_sleep', n.get_bool_value()),
            "startMenuHideSwitchAccount": lambda n : setattr(self, 'start_menu_hide_switch_account', n.get_bool_value()),
            "startMenuHideUserTile": lambda n : setattr(self, 'start_menu_hide_user_tile', n.get_bool_value()),
            "startMenuLayoutEdgeAssetsXml": lambda n : setattr(self, 'start_menu_layout_edge_assets_xml', n.get_bytes_value()),
            "startMenuLayoutXml": lambda n : setattr(self, 'start_menu_layout_xml', n.get_bytes_value()),
            "startMenuMode": lambda n : setattr(self, 'start_menu_mode', n.get_enum_value(windows_start_menu_mode_type.WindowsStartMenuModeType)),
            "startMenuPinnedFolderDocuments": lambda n : setattr(self, 'start_menu_pinned_folder_documents', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderDownloads": lambda n : setattr(self, 'start_menu_pinned_folder_downloads', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderFileExplorer": lambda n : setattr(self, 'start_menu_pinned_folder_file_explorer', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderHomeGroup": lambda n : setattr(self, 'start_menu_pinned_folder_home_group', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderMusic": lambda n : setattr(self, 'start_menu_pinned_folder_music', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderNetwork": lambda n : setattr(self, 'start_menu_pinned_folder_network', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderPersonalFolder": lambda n : setattr(self, 'start_menu_pinned_folder_personal_folder', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderPictures": lambda n : setattr(self, 'start_menu_pinned_folder_pictures', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderSettings": lambda n : setattr(self, 'start_menu_pinned_folder_settings', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "startMenuPinnedFolderVideos": lambda n : setattr(self, 'start_menu_pinned_folder_videos', n.get_enum_value(visibility_setting.VisibilitySetting)),
            "storageBlockRemovableStorage": lambda n : setattr(self, 'storage_block_removable_storage', n.get_bool_value()),
            "storageRequireMobileDeviceEncryption": lambda n : setattr(self, 'storage_require_mobile_device_encryption', n.get_bool_value()),
            "storageRestrictAppDataToSystemVolume": lambda n : setattr(self, 'storage_restrict_app_data_to_system_volume', n.get_bool_value()),
            "storageRestrictAppInstallToSystemVolume": lambda n : setattr(self, 'storage_restrict_app_install_to_system_volume', n.get_bool_value()),
            "tenantLockdownRequireNetworkDuringOutOfBoxExperience": lambda n : setattr(self, 'tenant_lockdown_require_network_during_out_of_box_experience', n.get_bool_value()),
            "usbBlocked": lambda n : setattr(self, 'usb_blocked', n.get_bool_value()),
            "voiceRecordingBlocked": lambda n : setattr(self, 'voice_recording_blocked', n.get_bool_value()),
            "webRtcBlockLocalhostIpAddress": lambda n : setattr(self, 'web_rtc_block_localhost_ip_address', n.get_bool_value()),
            "windowsSpotlightBlocked": lambda n : setattr(self, 'windows_spotlight_blocked', n.get_bool_value()),
            "windowsSpotlightBlockConsumerSpecificFeatures": lambda n : setattr(self, 'windows_spotlight_block_consumer_specific_features', n.get_bool_value()),
            "windowsSpotlightBlockOnActionCenter": lambda n : setattr(self, 'windows_spotlight_block_on_action_center', n.get_bool_value()),
            "windowsSpotlightBlockTailoredExperiences": lambda n : setattr(self, 'windows_spotlight_block_tailored_experiences', n.get_bool_value()),
            "windowsSpotlightBlockThirdPartyNotifications": lambda n : setattr(self, 'windows_spotlight_block_third_party_notifications', n.get_bool_value()),
            "windowsSpotlightBlockWelcomeExperience": lambda n : setattr(self, 'windows_spotlight_block_welcome_experience', n.get_bool_value()),
            "windowsSpotlightBlockWindowsTips": lambda n : setattr(self, 'windows_spotlight_block_windows_tips', n.get_bool_value()),
            "windowsSpotlightConfigureOnLockScreen": lambda n : setattr(self, 'windows_spotlight_configure_on_lock_screen', n.get_enum_value(windows_spotlight_enablement_settings.WindowsSpotlightEnablementSettings)),
            "windowsStoreBlocked": lambda n : setattr(self, 'windows_store_blocked', n.get_bool_value()),
            "windowsStoreBlockAutoUpdate": lambda n : setattr(self, 'windows_store_block_auto_update', n.get_bool_value()),
            "windowsStoreEnablePrivateStoreOnly": lambda n : setattr(self, 'windows_store_enable_private_store_only', n.get_bool_value()),
            "wirelessDisplayBlockProjectionToThisDevice": lambda n : setattr(self, 'wireless_display_block_projection_to_this_device', n.get_bool_value()),
            "wirelessDisplayBlockUserInputFromReceiver": lambda n : setattr(self, 'wireless_display_block_user_input_from_receiver', n.get_bool_value()),
            "wirelessDisplayRequirePinForPairing": lambda n : setattr(self, 'wireless_display_require_pin_for_pairing', n.get_bool_value()),
            "wiFiBlocked": lambda n : setattr(self, 'wi_fi_blocked', n.get_bool_value()),
            "wiFiBlockAutomaticConnectHotspots": lambda n : setattr(self, 'wi_fi_block_automatic_connect_hotspots', n.get_bool_value()),
            "wiFiBlockManualConfiguration": lambda n : setattr(self, 'wi_fi_block_manual_configuration', n.get_bool_value()),
            "wiFiScanInterval": lambda n : setattr(self, 'wi_fi_scan_interval', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def internet_sharing_blocked(self,) -> Optional[bool]:
        """
        Gets the internetSharingBlocked property value. Indicates whether or not to Block the user from using internet sharing.
        Returns: Optional[bool]
        """
        return self._internet_sharing_blocked
    
    @internet_sharing_blocked.setter
    def internet_sharing_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the internetSharingBlocked property value. Indicates whether or not to Block the user from using internet sharing.
        Args:
            value: Value to set for the internet_sharing_blocked property.
        """
        self._internet_sharing_blocked = value
    
    @property
    def location_services_blocked(self,) -> Optional[bool]:
        """
        Gets the locationServicesBlocked property value. Indicates whether or not to Block the user from location services.
        Returns: Optional[bool]
        """
        return self._location_services_blocked
    
    @location_services_blocked.setter
    def location_services_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the locationServicesBlocked property value. Indicates whether or not to Block the user from location services.
        Args:
            value: Value to set for the location_services_blocked property.
        """
        self._location_services_blocked = value
    
    @property
    def lock_screen_allow_timeout_configuration(self,) -> Optional[bool]:
        """
        Gets the lockScreenAllowTimeoutConfiguration property value. Specify whether to show a user-configurable setting to control the screen timeout while on the lock screen of Windows 10 Mobile devices. If this policy is set to Allow, the value set by lockScreenTimeoutInSeconds is ignored.
        Returns: Optional[bool]
        """
        return self._lock_screen_allow_timeout_configuration
    
    @lock_screen_allow_timeout_configuration.setter
    def lock_screen_allow_timeout_configuration(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenAllowTimeoutConfiguration property value. Specify whether to show a user-configurable setting to control the screen timeout while on the lock screen of Windows 10 Mobile devices. If this policy is set to Allow, the value set by lockScreenTimeoutInSeconds is ignored.
        Args:
            value: Value to set for the lock_screen_allow_timeout_configuration property.
        """
        self._lock_screen_allow_timeout_configuration = value
    
    @property
    def lock_screen_block_action_center_notifications(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockActionCenterNotifications property value. Indicates whether or not to block action center notifications over lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_action_center_notifications
    
    @lock_screen_block_action_center_notifications.setter
    def lock_screen_block_action_center_notifications(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockActionCenterNotifications property value. Indicates whether or not to block action center notifications over lock screen.
        Args:
            value: Value to set for the lock_screen_block_action_center_notifications property.
        """
        self._lock_screen_block_action_center_notifications = value
    
    @property
    def lock_screen_block_cortana(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockCortana property value. Indicates whether or not the user can interact with Cortana using speech while the system is locked.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_cortana
    
    @lock_screen_block_cortana.setter
    def lock_screen_block_cortana(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockCortana property value. Indicates whether or not the user can interact with Cortana using speech while the system is locked.
        Args:
            value: Value to set for the lock_screen_block_cortana property.
        """
        self._lock_screen_block_cortana = value
    
    @property
    def lock_screen_block_toast_notifications(self,) -> Optional[bool]:
        """
        Gets the lockScreenBlockToastNotifications property value. Indicates whether to allow toast notifications above the device lock screen.
        Returns: Optional[bool]
        """
        return self._lock_screen_block_toast_notifications
    
    @lock_screen_block_toast_notifications.setter
    def lock_screen_block_toast_notifications(self,value: Optional[bool] = None) -> None:
        """
        Sets the lockScreenBlockToastNotifications property value. Indicates whether to allow toast notifications above the device lock screen.
        Args:
            value: Value to set for the lock_screen_block_toast_notifications property.
        """
        self._lock_screen_block_toast_notifications = value
    
    @property
    def lock_screen_timeout_in_seconds(self,) -> Optional[int]:
        """
        Gets the lockScreenTimeoutInSeconds property value. Set the duration (in seconds) from the screen locking to the screen turning off for Windows 10 Mobile devices. Supported values are 11-1800. Valid values 11 to 1800
        Returns: Optional[int]
        """
        return self._lock_screen_timeout_in_seconds
    
    @lock_screen_timeout_in_seconds.setter
    def lock_screen_timeout_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the lockScreenTimeoutInSeconds property value. Set the duration (in seconds) from the screen locking to the screen turning off for Windows 10 Mobile devices. Supported values are 11-1800. Valid values 11 to 1800
        Args:
            value: Value to set for the lock_screen_timeout_in_seconds property.
        """
        self._lock_screen_timeout_in_seconds = value
    
    @property
    def logon_block_fast_user_switching(self,) -> Optional[bool]:
        """
        Gets the logonBlockFastUserSwitching property value. Disables the ability to quickly switch between users that are logged on simultaneously without logging off.
        Returns: Optional[bool]
        """
        return self._logon_block_fast_user_switching
    
    @logon_block_fast_user_switching.setter
    def logon_block_fast_user_switching(self,value: Optional[bool] = None) -> None:
        """
        Sets the logonBlockFastUserSwitching property value. Disables the ability to quickly switch between users that are logged on simultaneously without logging off.
        Args:
            value: Value to set for the logon_block_fast_user_switching property.
        """
        self._logon_block_fast_user_switching = value
    
    @property
    def microsoft_account_block_settings_sync(self,) -> Optional[bool]:
        """
        Gets the microsoftAccountBlockSettingsSync property value. Indicates whether or not to Block Microsoft account settings sync.
        Returns: Optional[bool]
        """
        return self._microsoft_account_block_settings_sync
    
    @microsoft_account_block_settings_sync.setter
    def microsoft_account_block_settings_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftAccountBlockSettingsSync property value. Indicates whether or not to Block Microsoft account settings sync.
        Args:
            value: Value to set for the microsoft_account_block_settings_sync property.
        """
        self._microsoft_account_block_settings_sync = value
    
    @property
    def microsoft_account_blocked(self,) -> Optional[bool]:
        """
        Gets the microsoftAccountBlocked property value. Indicates whether or not to Block a Microsoft account.
        Returns: Optional[bool]
        """
        return self._microsoft_account_blocked
    
    @microsoft_account_blocked.setter
    def microsoft_account_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftAccountBlocked property value. Indicates whether or not to Block a Microsoft account.
        Args:
            value: Value to set for the microsoft_account_blocked property.
        """
        self._microsoft_account_blocked = value
    
    @property
    def network_proxy_apply_settings_device_wide(self,) -> Optional[bool]:
        """
        Gets the networkProxyApplySettingsDeviceWide property value. If set, proxy settings will be applied to all processes and accounts in the device. Otherwise, it will be applied to the user account that’s enrolled into MDM.
        Returns: Optional[bool]
        """
        return self._network_proxy_apply_settings_device_wide
    
    @network_proxy_apply_settings_device_wide.setter
    def network_proxy_apply_settings_device_wide(self,value: Optional[bool] = None) -> None:
        """
        Sets the networkProxyApplySettingsDeviceWide property value. If set, proxy settings will be applied to all processes and accounts in the device. Otherwise, it will be applied to the user account that’s enrolled into MDM.
        Args:
            value: Value to set for the network_proxy_apply_settings_device_wide property.
        """
        self._network_proxy_apply_settings_device_wide = value
    
    @property
    def network_proxy_automatic_configuration_url(self,) -> Optional[str]:
        """
        Gets the networkProxyAutomaticConfigurationUrl property value. Address to the proxy auto-config (PAC) script you want to use.
        Returns: Optional[str]
        """
        return self._network_proxy_automatic_configuration_url
    
    @network_proxy_automatic_configuration_url.setter
    def network_proxy_automatic_configuration_url(self,value: Optional[str] = None) -> None:
        """
        Sets the networkProxyAutomaticConfigurationUrl property value. Address to the proxy auto-config (PAC) script you want to use.
        Args:
            value: Value to set for the network_proxy_automatic_configuration_url property.
        """
        self._network_proxy_automatic_configuration_url = value
    
    @property
    def network_proxy_disable_auto_detect(self,) -> Optional[bool]:
        """
        Gets the networkProxyDisableAutoDetect property value. Disable automatic detection of settings. If enabled, the system will try to find the path to a proxy auto-config (PAC) script.
        Returns: Optional[bool]
        """
        return self._network_proxy_disable_auto_detect
    
    @network_proxy_disable_auto_detect.setter
    def network_proxy_disable_auto_detect(self,value: Optional[bool] = None) -> None:
        """
        Sets the networkProxyDisableAutoDetect property value. Disable automatic detection of settings. If enabled, the system will try to find the path to a proxy auto-config (PAC) script.
        Args:
            value: Value to set for the network_proxy_disable_auto_detect property.
        """
        self._network_proxy_disable_auto_detect = value
    
    @property
    def network_proxy_server(self,) -> Optional[windows10_network_proxy_server.Windows10NetworkProxyServer]:
        """
        Gets the networkProxyServer property value. Specifies manual proxy server settings.
        Returns: Optional[windows10_network_proxy_server.Windows10NetworkProxyServer]
        """
        return self._network_proxy_server
    
    @network_proxy_server.setter
    def network_proxy_server(self,value: Optional[windows10_network_proxy_server.Windows10NetworkProxyServer] = None) -> None:
        """
        Sets the networkProxyServer property value. Specifies manual proxy server settings.
        Args:
            value: Value to set for the network_proxy_server property.
        """
        self._network_proxy_server = value
    
    @property
    def nfc_blocked(self,) -> Optional[bool]:
        """
        Gets the nfcBlocked property value. Indicates whether or not to Block the user from using near field communication.
        Returns: Optional[bool]
        """
        return self._nfc_blocked
    
    @nfc_blocked.setter
    def nfc_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the nfcBlocked property value. Indicates whether or not to Block the user from using near field communication.
        Args:
            value: Value to set for the nfc_blocked property.
        """
        self._nfc_blocked = value
    
    @property
    def one_drive_disable_file_sync(self,) -> Optional[bool]:
        """
        Gets the oneDriveDisableFileSync property value. Gets or sets a value allowing IT admins to prevent apps and features from working with files on OneDrive.
        Returns: Optional[bool]
        """
        return self._one_drive_disable_file_sync
    
    @one_drive_disable_file_sync.setter
    def one_drive_disable_file_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the oneDriveDisableFileSync property value. Gets or sets a value allowing IT admins to prevent apps and features from working with files on OneDrive.
        Args:
            value: Value to set for the one_drive_disable_file_sync property.
        """
        self._one_drive_disable_file_sync = value
    
    @property
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Specify whether PINs or passwords such as '1111' or '1234' are allowed. For Windows 10 desktops, it also controls the use of picture passwords.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Specify whether PINs or passwords such as '1111' or '1234' are allowed. For Windows 10 desktops, it also controls the use of picture passwords.
        Args:
            value: Value to set for the password_block_simple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. The password expiration in days. Valid values 0 to 730
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. The password expiration in days. Valid values 0 to 730
        Args:
            value: Value to set for the password_expiration_days property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Args:
            value: Value to set for the password_minimum_character_set_count property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. The minimum password length. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. The minimum password length. Valid values 4 to 16
        Args:
            value: Value to set for the password_minimum_length property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeScreenTimeout property value. The minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_screen_timeout
    
    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeScreenTimeout property value. The minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the password_minutes_of_inactivity_before_screen_timeout property.
        """
        self._password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent reuse of. Valid values 0 to 50
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent reuse of. Valid values 0 to 50
        Args:
            value: Value to set for the password_previous_password_block_count property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_require_when_resume_from_idle_state(self,) -> Optional[bool]:
        """
        Gets the passwordRequireWhenResumeFromIdleState property value. Indicates whether or not to require a password upon resuming from an idle state.
        Returns: Optional[bool]
        """
        return self._password_require_when_resume_from_idle_state
    
    @password_require_when_resume_from_idle_state.setter
    def password_require_when_resume_from_idle_state(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequireWhenResumeFromIdleState property value. Indicates whether or not to require a password upon resuming from an idle state.
        Args:
            value: Value to set for the password_require_when_resume_from_idle_state property.
        """
        self._password_require_when_resume_from_idle_state = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Indicates whether or not to require the user to have a password.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Indicates whether or not to require the user to have a password.
        Args:
            value: Value to set for the password_required property.
        """
        self._password_required = value
    
    @property
    def password_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the password_required_type property.
        """
        self._password_required_type = value
    
    @property
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. The number of sign in failures before factory reset. Valid values 0 to 999
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. The number of sign in failures before factory reset. Valid values 0 to 999
        Args:
            value: Value to set for the password_sign_in_failure_count_before_factory_reset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
    @property
    def personalization_desktop_image_url(self,) -> Optional[str]:
        """
        Gets the personalizationDesktopImageUrl property value. A http or https Url to a jpg, jpeg or png image that needs to be downloaded and used as the Desktop Image or a file Url to a local image on the file system that needs to used as the Desktop Image.
        Returns: Optional[str]
        """
        return self._personalization_desktop_image_url
    
    @personalization_desktop_image_url.setter
    def personalization_desktop_image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the personalizationDesktopImageUrl property value. A http or https Url to a jpg, jpeg or png image that needs to be downloaded and used as the Desktop Image or a file Url to a local image on the file system that needs to used as the Desktop Image.
        Args:
            value: Value to set for the personalization_desktop_image_url property.
        """
        self._personalization_desktop_image_url = value
    
    @property
    def personalization_lock_screen_image_url(self,) -> Optional[str]:
        """
        Gets the personalizationLockScreenImageUrl property value. A http or https Url to a jpg, jpeg or png image that neeeds to be downloaded and used as the Lock Screen Image or a file Url to a local image on the file system that needs to be used as the Lock Screen Image.
        Returns: Optional[str]
        """
        return self._personalization_lock_screen_image_url
    
    @personalization_lock_screen_image_url.setter
    def personalization_lock_screen_image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the personalizationLockScreenImageUrl property value. A http or https Url to a jpg, jpeg or png image that neeeds to be downloaded and used as the Lock Screen Image or a file Url to a local image on the file system that needs to be used as the Lock Screen Image.
        Args:
            value: Value to set for the personalization_lock_screen_image_url property.
        """
        self._personalization_lock_screen_image_url = value
    
    @property
    def privacy_advertising_id(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the privacyAdvertisingId property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._privacy_advertising_id
    
    @privacy_advertising_id.setter
    def privacy_advertising_id(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the privacyAdvertisingId property value. State Management Setting.
        Args:
            value: Value to set for the privacy_advertising_id property.
        """
        self._privacy_advertising_id = value
    
    @property
    def privacy_auto_accept_pairing_and_consent_prompts(self,) -> Optional[bool]:
        """
        Gets the privacyAutoAcceptPairingAndConsentPrompts property value. Indicates whether or not to allow the automatic acceptance of the pairing and privacy user consent dialog when launching apps.
        Returns: Optional[bool]
        """
        return self._privacy_auto_accept_pairing_and_consent_prompts
    
    @privacy_auto_accept_pairing_and_consent_prompts.setter
    def privacy_auto_accept_pairing_and_consent_prompts(self,value: Optional[bool] = None) -> None:
        """
        Sets the privacyAutoAcceptPairingAndConsentPrompts property value. Indicates whether or not to allow the automatic acceptance of the pairing and privacy user consent dialog when launching apps.
        Args:
            value: Value to set for the privacy_auto_accept_pairing_and_consent_prompts property.
        """
        self._privacy_auto_accept_pairing_and_consent_prompts = value
    
    @property
    def privacy_block_input_personalization(self,) -> Optional[bool]:
        """
        Gets the privacyBlockInputPersonalization property value. Indicates whether or not to block the usage of cloud based speech services for Cortana, Dictation, or Store applications.
        Returns: Optional[bool]
        """
        return self._privacy_block_input_personalization
    
    @privacy_block_input_personalization.setter
    def privacy_block_input_personalization(self,value: Optional[bool] = None) -> None:
        """
        Sets the privacyBlockInputPersonalization property value. Indicates whether or not to block the usage of cloud based speech services for Cortana, Dictation, or Store applications.
        Args:
            value: Value to set for the privacy_block_input_personalization property.
        """
        self._privacy_block_input_personalization = value
    
    @property
    def reset_protection_mode_blocked(self,) -> Optional[bool]:
        """
        Gets the resetProtectionModeBlocked property value. Indicates whether or not to Block the user from reset protection mode.
        Returns: Optional[bool]
        """
        return self._reset_protection_mode_blocked
    
    @reset_protection_mode_blocked.setter
    def reset_protection_mode_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the resetProtectionModeBlocked property value. Indicates whether or not to Block the user from reset protection mode.
        Args:
            value: Value to set for the reset_protection_mode_blocked property.
        """
        self._reset_protection_mode_blocked = value
    
    @property
    def safe_search_filter(self,) -> Optional[safe_search_filter_type.SafeSearchFilterType]:
        """
        Gets the safeSearchFilter property value. Specifies what level of safe search (filtering adult content) is required
        Returns: Optional[safe_search_filter_type.SafeSearchFilterType]
        """
        return self._safe_search_filter
    
    @safe_search_filter.setter
    def safe_search_filter(self,value: Optional[safe_search_filter_type.SafeSearchFilterType] = None) -> None:
        """
        Sets the safeSearchFilter property value. Specifies what level of safe search (filtering adult content) is required
        Args:
            value: Value to set for the safe_search_filter property.
        """
        self._safe_search_filter = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether or not to Block the user from taking Screenshots.
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether or not to Block the user from taking Screenshots.
        Args:
            value: Value to set for the screen_capture_blocked property.
        """
        self._screen_capture_blocked = value
    
    @property
    def search_block_diacritics(self,) -> Optional[bool]:
        """
        Gets the searchBlockDiacritics property value. Specifies if search can use diacritics.
        Returns: Optional[bool]
        """
        return self._search_block_diacritics
    
    @search_block_diacritics.setter
    def search_block_diacritics(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchBlockDiacritics property value. Specifies if search can use diacritics.
        Args:
            value: Value to set for the search_block_diacritics property.
        """
        self._search_block_diacritics = value
    
    @property
    def search_disable_auto_language_detection(self,) -> Optional[bool]:
        """
        Gets the searchDisableAutoLanguageDetection property value. Specifies whether to use automatic language detection when indexing content and properties.
        Returns: Optional[bool]
        """
        return self._search_disable_auto_language_detection
    
    @search_disable_auto_language_detection.setter
    def search_disable_auto_language_detection(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchDisableAutoLanguageDetection property value. Specifies whether to use automatic language detection when indexing content and properties.
        Args:
            value: Value to set for the search_disable_auto_language_detection property.
        """
        self._search_disable_auto_language_detection = value
    
    @property
    def search_disable_indexer_backoff(self,) -> Optional[bool]:
        """
        Gets the searchDisableIndexerBackoff property value. Indicates whether or not to disable the search indexer backoff feature.
        Returns: Optional[bool]
        """
        return self._search_disable_indexer_backoff
    
    @search_disable_indexer_backoff.setter
    def search_disable_indexer_backoff(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchDisableIndexerBackoff property value. Indicates whether or not to disable the search indexer backoff feature.
        Args:
            value: Value to set for the search_disable_indexer_backoff property.
        """
        self._search_disable_indexer_backoff = value
    
    @property
    def search_disable_indexing_encrypted_items(self,) -> Optional[bool]:
        """
        Gets the searchDisableIndexingEncryptedItems property value. Indicates whether or not to block indexing of WIP-protected items to prevent them from appearing in search results for Cortana or Explorer.
        Returns: Optional[bool]
        """
        return self._search_disable_indexing_encrypted_items
    
    @search_disable_indexing_encrypted_items.setter
    def search_disable_indexing_encrypted_items(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchDisableIndexingEncryptedItems property value. Indicates whether or not to block indexing of WIP-protected items to prevent them from appearing in search results for Cortana or Explorer.
        Args:
            value: Value to set for the search_disable_indexing_encrypted_items property.
        """
        self._search_disable_indexing_encrypted_items = value
    
    @property
    def search_disable_indexing_removable_drive(self,) -> Optional[bool]:
        """
        Gets the searchDisableIndexingRemovableDrive property value. Indicates whether or not to allow users to add locations on removable drives to libraries and to be indexed.
        Returns: Optional[bool]
        """
        return self._search_disable_indexing_removable_drive
    
    @search_disable_indexing_removable_drive.setter
    def search_disable_indexing_removable_drive(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchDisableIndexingRemovableDrive property value. Indicates whether or not to allow users to add locations on removable drives to libraries and to be indexed.
        Args:
            value: Value to set for the search_disable_indexing_removable_drive property.
        """
        self._search_disable_indexing_removable_drive = value
    
    @property
    def search_enable_automatic_index_size_manangement(self,) -> Optional[bool]:
        """
        Gets the searchEnableAutomaticIndexSizeManangement property value. Specifies minimum amount of hard drive space on the same drive as the index location before indexing stops.
        Returns: Optional[bool]
        """
        return self._search_enable_automatic_index_size_manangement
    
    @search_enable_automatic_index_size_manangement.setter
    def search_enable_automatic_index_size_manangement(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchEnableAutomaticIndexSizeManangement property value. Specifies minimum amount of hard drive space on the same drive as the index location before indexing stops.
        Args:
            value: Value to set for the search_enable_automatic_index_size_manangement property.
        """
        self._search_enable_automatic_index_size_manangement = value
    
    @property
    def search_enable_remote_queries(self,) -> Optional[bool]:
        """
        Gets the searchEnableRemoteQueries property value. Indicates whether or not to block remote queries of this computer’s index.
        Returns: Optional[bool]
        """
        return self._search_enable_remote_queries
    
    @search_enable_remote_queries.setter
    def search_enable_remote_queries(self,value: Optional[bool] = None) -> None:
        """
        Sets the searchEnableRemoteQueries property value. Indicates whether or not to block remote queries of this computer’s index.
        Args:
            value: Value to set for the search_enable_remote_queries property.
        """
        self._search_enable_remote_queries = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("accountsBlockAddingNonMicrosoftAccountEmail", self.accounts_block_adding_non_microsoft_account_email)
        writer.write_bool_value("antiTheftModeBlocked", self.anti_theft_mode_blocked)
        writer.write_enum_value("appsAllowTrustedAppsSideloading", self.apps_allow_trusted_apps_sideloading)
        writer.write_bool_value("appsBlockWindowsStoreOriginatedApps", self.apps_block_windows_store_originated_apps)
        writer.write_collection_of_primitive_values("bluetoothAllowedServices", self.bluetooth_allowed_services)
        writer.write_bool_value("bluetoothBlocked", self.bluetooth_blocked)
        writer.write_bool_value("bluetoothBlockAdvertising", self.bluetooth_block_advertising)
        writer.write_bool_value("bluetoothBlockDiscoverableMode", self.bluetooth_block_discoverable_mode)
        writer.write_bool_value("bluetoothBlockPrePairing", self.bluetooth_block_pre_pairing)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockDataWhenRoaming", self.cellular_block_data_when_roaming)
        writer.write_bool_value("cellularBlockVpn", self.cellular_block_vpn)
        writer.write_bool_value("cellularBlockVpnWhenRoaming", self.cellular_block_vpn_when_roaming)
        writer.write_bool_value("certificatesBlockManualRootCertificateInstallation", self.certificates_block_manual_root_certificate_installation)
        writer.write_bool_value("connectedDevicesServiceBlocked", self.connected_devices_service_blocked)
        writer.write_bool_value("copyPasteBlocked", self.copy_paste_blocked)
        writer.write_bool_value("cortanaBlocked", self.cortana_blocked)
        writer.write_bool_value("defenderBlockEndUserAccess", self.defender_block_end_user_access)
        writer.write_enum_value("defenderCloudBlockLevel", self.defender_cloud_block_level)
        writer.write_int_value("defenderDaysBeforeDeletingQuarantinedMalware", self.defender_days_before_deleting_quarantined_malware)
        writer.write_object_value("defenderDetectedMalwareActions", self.defender_detected_malware_actions)
        writer.write_collection_of_primitive_values("defenderFilesAndFoldersToExclude", self.defender_files_and_folders_to_exclude)
        writer.write_collection_of_primitive_values("defenderFileExtensionsToExclude", self.defender_file_extensions_to_exclude)
        writer.write_enum_value("defenderMonitorFileActivity", self.defender_monitor_file_activity)
        writer.write_collection_of_primitive_values("defenderProcessesToExclude", self.defender_processes_to_exclude)
        writer.write_enum_value("defenderPromptForSampleSubmission", self.defender_prompt_for_sample_submission)
        writer.write_bool_value("defenderRequireBehaviorMonitoring", self.defender_require_behavior_monitoring)
        writer.write_bool_value("defenderRequireCloudProtection", self.defender_require_cloud_protection)
        writer.write_bool_value("defenderRequireNetworkInspectionSystem", self.defender_require_network_inspection_system)
        writer.write_bool_value("defenderRequireRealTimeMonitoring", self.defender_require_real_time_monitoring)
        writer.write_bool_value("defenderScanArchiveFiles", self.defender_scan_archive_files)
        writer.write_bool_value("defenderScanDownloads", self.defender_scan_downloads)
        writer.write_bool_value("defenderScanIncomingMail", self.defender_scan_incoming_mail)
        writer.write_bool_value("defenderScanMappedNetworkDrivesDuringFullScan", self.defender_scan_mapped_network_drives_during_full_scan)
        writer.write_int_value("defenderScanMaxCpu", self.defender_scan_max_cpu)
        writer.write_bool_value("defenderScanNetworkFiles", self.defender_scan_network_files)
        writer.write_bool_value("defenderScanRemovableDrivesDuringFullScan", self.defender_scan_removable_drives_during_full_scan)
        writer.write_bool_value("defenderScanScriptsLoadedInInternetExplorer", self.defender_scan_scripts_loaded_in_internet_explorer)
        writer.write_enum_value("defenderScanType", self.defender_scan_type)
        writer.write_time_value("defenderScheduledQuickScanTime", self.defender_scheduled_quick_scan_time)
        writer.write_time_value("defenderScheduledScanTime", self.defender_scheduled_scan_time)
        writer.write_int_value("defenderSignatureUpdateIntervalInHours", self.defender_signature_update_interval_in_hours)
        writer.write_enum_value("defenderSystemScanSchedule", self.defender_system_scan_schedule)
        writer.write_enum_value("developerUnlockSetting", self.developer_unlock_setting)
        writer.write_bool_value("deviceManagementBlockFactoryResetOnMobile", self.device_management_block_factory_reset_on_mobile)
        writer.write_bool_value("deviceManagementBlockManualUnenroll", self.device_management_block_manual_unenroll)
        writer.write_enum_value("diagnosticsDataSubmissionMode", self.diagnostics_data_submission_mode)
        writer.write_bool_value("edgeAllowStartPagesModification", self.edge_allow_start_pages_modification)
        writer.write_bool_value("edgeBlocked", self.edge_blocked)
        writer.write_bool_value("edgeBlockAccessToAboutFlags", self.edge_block_access_to_about_flags)
        writer.write_bool_value("edgeBlockAddressBarDropdown", self.edge_block_address_bar_dropdown)
        writer.write_bool_value("edgeBlockAutofill", self.edge_block_autofill)
        writer.write_bool_value("edgeBlockCompatibilityList", self.edge_block_compatibility_list)
        writer.write_bool_value("edgeBlockDeveloperTools", self.edge_block_developer_tools)
        writer.write_bool_value("edgeBlockExtensions", self.edge_block_extensions)
        writer.write_bool_value("edgeBlockInPrivateBrowsing", self.edge_block_in_private_browsing)
        writer.write_bool_value("edgeBlockJavaScript", self.edge_block_java_script)
        writer.write_bool_value("edgeBlockLiveTileDataCollection", self.edge_block_live_tile_data_collection)
        writer.write_bool_value("edgeBlockPasswordManager", self.edge_block_password_manager)
        writer.write_bool_value("edgeBlockPopups", self.edge_block_popups)
        writer.write_bool_value("edgeBlockSearchSuggestions", self.edge_block_search_suggestions)
        writer.write_bool_value("edgeBlockSendingDoNotTrackHeader", self.edge_block_sending_do_not_track_header)
        writer.write_bool_value("edgeBlockSendingIntranetTrafficToInternetExplorer", self.edge_block_sending_intranet_traffic_to_internet_explorer)
        writer.write_bool_value("edgeClearBrowsingDataOnExit", self.edge_clear_browsing_data_on_exit)
        writer.write_enum_value("edgeCookiePolicy", self.edge_cookie_policy)
        writer.write_bool_value("edgeDisableFirstRunPage", self.edge_disable_first_run_page)
        writer.write_str_value("edgeEnterpriseModeSiteListLocation", self.edge_enterprise_mode_site_list_location)
        writer.write_str_value("edgeFirstRunUrl", self.edge_first_run_url)
        writer.write_collection_of_primitive_values("edgeHomepageUrls", self.edge_homepage_urls)
        writer.write_bool_value("edgeRequireSmartScreen", self.edge_require_smart_screen)
        writer.write_object_value("edgeSearchEngine", self.edge_search_engine)
        writer.write_bool_value("edgeSendIntranetTrafficToInternetExplorer", self.edge_send_intranet_traffic_to_internet_explorer)
        writer.write_bool_value("edgeSyncFavoritesWithInternetExplorer", self.edge_sync_favorites_with_internet_explorer)
        writer.write_str_value("enterpriseCloudPrintDiscoveryEndPoint", self.enterprise_cloud_print_discovery_end_point)
        writer.write_int_value("enterpriseCloudPrintDiscoveryMaxLimit", self.enterprise_cloud_print_discovery_max_limit)
        writer.write_str_value("enterpriseCloudPrintMopriaDiscoveryResourceIdentifier", self.enterprise_cloud_print_mopria_discovery_resource_identifier)
        writer.write_str_value("enterpriseCloudPrintOAuthAuthority", self.enterprise_cloud_print_o_auth_authority)
        writer.write_str_value("enterpriseCloudPrintOAuthClientIdentifier", self.enterprise_cloud_print_o_auth_client_identifier)
        writer.write_str_value("enterpriseCloudPrintResourceIdentifier", self.enterprise_cloud_print_resource_identifier)
        writer.write_bool_value("experienceBlockDeviceDiscovery", self.experience_block_device_discovery)
        writer.write_bool_value("experienceBlockErrorDialogWhenNoSIM", self.experience_block_error_dialog_when_no_s_i_m)
        writer.write_bool_value("experienceBlockTaskSwitcher", self.experience_block_task_switcher)
        writer.write_bool_value("gameDvrBlocked", self.game_dvr_blocked)
        writer.write_bool_value("internetSharingBlocked", self.internet_sharing_blocked)
        writer.write_bool_value("locationServicesBlocked", self.location_services_blocked)
        writer.write_bool_value("lockScreenAllowTimeoutConfiguration", self.lock_screen_allow_timeout_configuration)
        writer.write_bool_value("lockScreenBlockActionCenterNotifications", self.lock_screen_block_action_center_notifications)
        writer.write_bool_value("lockScreenBlockCortana", self.lock_screen_block_cortana)
        writer.write_bool_value("lockScreenBlockToastNotifications", self.lock_screen_block_toast_notifications)
        writer.write_int_value("lockScreenTimeoutInSeconds", self.lock_screen_timeout_in_seconds)
        writer.write_bool_value("logonBlockFastUserSwitching", self.logon_block_fast_user_switching)
        writer.write_bool_value("microsoftAccountBlocked", self.microsoft_account_blocked)
        writer.write_bool_value("microsoftAccountBlockSettingsSync", self.microsoft_account_block_settings_sync)
        writer.write_bool_value("networkProxyApplySettingsDeviceWide", self.network_proxy_apply_settings_device_wide)
        writer.write_str_value("networkProxyAutomaticConfigurationUrl", self.network_proxy_automatic_configuration_url)
        writer.write_bool_value("networkProxyDisableAutoDetect", self.network_proxy_disable_auto_detect)
        writer.write_object_value("networkProxyServer", self.network_proxy_server)
        writer.write_bool_value("nfcBlocked", self.nfc_blocked)
        writer.write_bool_value("oneDriveDisableFileSync", self.one_drive_disable_file_sync)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("passwordRequireWhenResumeFromIdleState", self.password_require_when_resume_from_idle_state)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_str_value("personalizationDesktopImageUrl", self.personalization_desktop_image_url)
        writer.write_str_value("personalizationLockScreenImageUrl", self.personalization_lock_screen_image_url)
        writer.write_enum_value("privacyAdvertisingId", self.privacy_advertising_id)
        writer.write_bool_value("privacyAutoAcceptPairingAndConsentPrompts", self.privacy_auto_accept_pairing_and_consent_prompts)
        writer.write_bool_value("privacyBlockInputPersonalization", self.privacy_block_input_personalization)
        writer.write_bool_value("resetProtectionModeBlocked", self.reset_protection_mode_blocked)
        writer.write_enum_value("safeSearchFilter", self.safe_search_filter)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("searchBlockDiacritics", self.search_block_diacritics)
        writer.write_bool_value("searchDisableAutoLanguageDetection", self.search_disable_auto_language_detection)
        writer.write_bool_value("searchDisableIndexerBackoff", self.search_disable_indexer_backoff)
        writer.write_bool_value("searchDisableIndexingEncryptedItems", self.search_disable_indexing_encrypted_items)
        writer.write_bool_value("searchDisableIndexingRemovableDrive", self.search_disable_indexing_removable_drive)
        writer.write_bool_value("searchEnableAutomaticIndexSizeManangement", self.search_enable_automatic_index_size_manangement)
        writer.write_bool_value("searchEnableRemoteQueries", self.search_enable_remote_queries)
        writer.write_bool_value("settingsBlockAccountsPage", self.settings_block_accounts_page)
        writer.write_bool_value("settingsBlockAddProvisioningPackage", self.settings_block_add_provisioning_package)
        writer.write_bool_value("settingsBlockAppsPage", self.settings_block_apps_page)
        writer.write_bool_value("settingsBlockChangeLanguage", self.settings_block_change_language)
        writer.write_bool_value("settingsBlockChangePowerSleep", self.settings_block_change_power_sleep)
        writer.write_bool_value("settingsBlockChangeRegion", self.settings_block_change_region)
        writer.write_bool_value("settingsBlockChangeSystemTime", self.settings_block_change_system_time)
        writer.write_bool_value("settingsBlockDevicesPage", self.settings_block_devices_page)
        writer.write_bool_value("settingsBlockEaseOfAccessPage", self.settings_block_ease_of_access_page)
        writer.write_bool_value("settingsBlockEditDeviceName", self.settings_block_edit_device_name)
        writer.write_bool_value("settingsBlockGamingPage", self.settings_block_gaming_page)
        writer.write_bool_value("settingsBlockNetworkInternetPage", self.settings_block_network_internet_page)
        writer.write_bool_value("settingsBlockPersonalizationPage", self.settings_block_personalization_page)
        writer.write_bool_value("settingsBlockPrivacyPage", self.settings_block_privacy_page)
        writer.write_bool_value("settingsBlockRemoveProvisioningPackage", self.settings_block_remove_provisioning_package)
        writer.write_bool_value("settingsBlockSettingsApp", self.settings_block_settings_app)
        writer.write_bool_value("settingsBlockSystemPage", self.settings_block_system_page)
        writer.write_bool_value("settingsBlockTimeLanguagePage", self.settings_block_time_language_page)
        writer.write_bool_value("settingsBlockUpdateSecurityPage", self.settings_block_update_security_page)
        writer.write_bool_value("sharedUserAppDataAllowed", self.shared_user_app_data_allowed)
        writer.write_bool_value("smartScreenBlockPromptOverride", self.smart_screen_block_prompt_override)
        writer.write_bool_value("smartScreenBlockPromptOverrideForFiles", self.smart_screen_block_prompt_override_for_files)
        writer.write_bool_value("smartScreenEnableAppInstallControl", self.smart_screen_enable_app_install_control)
        writer.write_bool_value("startBlockUnpinningAppsFromTaskbar", self.start_block_unpinning_apps_from_taskbar)
        writer.write_enum_value("startMenuAppListVisibility", self.start_menu_app_list_visibility)
        writer.write_bool_value("startMenuHideChangeAccountSettings", self.start_menu_hide_change_account_settings)
        writer.write_bool_value("startMenuHideFrequentlyUsedApps", self.start_menu_hide_frequently_used_apps)
        writer.write_bool_value("startMenuHideHibernate", self.start_menu_hide_hibernate)
        writer.write_bool_value("startMenuHideLock", self.start_menu_hide_lock)
        writer.write_bool_value("startMenuHidePowerButton", self.start_menu_hide_power_button)
        writer.write_bool_value("startMenuHideRecentlyAddedApps", self.start_menu_hide_recently_added_apps)
        writer.write_bool_value("startMenuHideRecentJumpLists", self.start_menu_hide_recent_jump_lists)
        writer.write_bool_value("startMenuHideRestartOptions", self.start_menu_hide_restart_options)
        writer.write_bool_value("startMenuHideShutDown", self.start_menu_hide_shut_down)
        writer.write_bool_value("startMenuHideSignOut", self.start_menu_hide_sign_out)
        writer.write_bool_value("startMenuHideSleep", self.start_menu_hide_sleep)
        writer.write_bool_value("startMenuHideSwitchAccount", self.start_menu_hide_switch_account)
        writer.write_bool_value("startMenuHideUserTile", self.start_menu_hide_user_tile)
        writer.write_object_value("startMenuLayoutEdgeAssetsXml", self.start_menu_layout_edge_assets_xml)
        writer.write_object_value("startMenuLayoutXml", self.start_menu_layout_xml)
        writer.write_enum_value("startMenuMode", self.start_menu_mode)
        writer.write_enum_value("startMenuPinnedFolderDocuments", self.start_menu_pinned_folder_documents)
        writer.write_enum_value("startMenuPinnedFolderDownloads", self.start_menu_pinned_folder_downloads)
        writer.write_enum_value("startMenuPinnedFolderFileExplorer", self.start_menu_pinned_folder_file_explorer)
        writer.write_enum_value("startMenuPinnedFolderHomeGroup", self.start_menu_pinned_folder_home_group)
        writer.write_enum_value("startMenuPinnedFolderMusic", self.start_menu_pinned_folder_music)
        writer.write_enum_value("startMenuPinnedFolderNetwork", self.start_menu_pinned_folder_network)
        writer.write_enum_value("startMenuPinnedFolderPersonalFolder", self.start_menu_pinned_folder_personal_folder)
        writer.write_enum_value("startMenuPinnedFolderPictures", self.start_menu_pinned_folder_pictures)
        writer.write_enum_value("startMenuPinnedFolderSettings", self.start_menu_pinned_folder_settings)
        writer.write_enum_value("startMenuPinnedFolderVideos", self.start_menu_pinned_folder_videos)
        writer.write_bool_value("storageBlockRemovableStorage", self.storage_block_removable_storage)
        writer.write_bool_value("storageRequireMobileDeviceEncryption", self.storage_require_mobile_device_encryption)
        writer.write_bool_value("storageRestrictAppDataToSystemVolume", self.storage_restrict_app_data_to_system_volume)
        writer.write_bool_value("storageRestrictAppInstallToSystemVolume", self.storage_restrict_app_install_to_system_volume)
        writer.write_bool_value("tenantLockdownRequireNetworkDuringOutOfBoxExperience", self.tenant_lockdown_require_network_during_out_of_box_experience)
        writer.write_bool_value("usbBlocked", self.usb_blocked)
        writer.write_bool_value("voiceRecordingBlocked", self.voice_recording_blocked)
        writer.write_bool_value("webRtcBlockLocalhostIpAddress", self.web_rtc_block_localhost_ip_address)
        writer.write_bool_value("windowsSpotlightBlocked", self.windows_spotlight_blocked)
        writer.write_bool_value("windowsSpotlightBlockConsumerSpecificFeatures", self.windows_spotlight_block_consumer_specific_features)
        writer.write_bool_value("windowsSpotlightBlockOnActionCenter", self.windows_spotlight_block_on_action_center)
        writer.write_bool_value("windowsSpotlightBlockTailoredExperiences", self.windows_spotlight_block_tailored_experiences)
        writer.write_bool_value("windowsSpotlightBlockThirdPartyNotifications", self.windows_spotlight_block_third_party_notifications)
        writer.write_bool_value("windowsSpotlightBlockWelcomeExperience", self.windows_spotlight_block_welcome_experience)
        writer.write_bool_value("windowsSpotlightBlockWindowsTips", self.windows_spotlight_block_windows_tips)
        writer.write_enum_value("windowsSpotlightConfigureOnLockScreen", self.windows_spotlight_configure_on_lock_screen)
        writer.write_bool_value("windowsStoreBlocked", self.windows_store_blocked)
        writer.write_bool_value("windowsStoreBlockAutoUpdate", self.windows_store_block_auto_update)
        writer.write_bool_value("windowsStoreEnablePrivateStoreOnly", self.windows_store_enable_private_store_only)
        writer.write_bool_value("wirelessDisplayBlockProjectionToThisDevice", self.wireless_display_block_projection_to_this_device)
        writer.write_bool_value("wirelessDisplayBlockUserInputFromReceiver", self.wireless_display_block_user_input_from_receiver)
        writer.write_bool_value("wirelessDisplayRequirePinForPairing", self.wireless_display_require_pin_for_pairing)
        writer.write_bool_value("wiFiBlocked", self.wi_fi_blocked)
        writer.write_bool_value("wiFiBlockAutomaticConnectHotspots", self.wi_fi_block_automatic_connect_hotspots)
        writer.write_bool_value("wiFiBlockManualConfiguration", self.wi_fi_block_manual_configuration)
        writer.write_int_value("wiFiScanInterval", self.wi_fi_scan_interval)
    
    @property
    def settings_block_accounts_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockAccountsPage property value. Indicates whether or not to block access to Accounts in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_accounts_page
    
    @settings_block_accounts_page.setter
    def settings_block_accounts_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockAccountsPage property value. Indicates whether or not to block access to Accounts in Settings app.
        Args:
            value: Value to set for the settings_block_accounts_page property.
        """
        self._settings_block_accounts_page = value
    
    @property
    def settings_block_add_provisioning_package(self,) -> Optional[bool]:
        """
        Gets the settingsBlockAddProvisioningPackage property value. Indicates whether or not to block the user from installing provisioning packages.
        Returns: Optional[bool]
        """
        return self._settings_block_add_provisioning_package
    
    @settings_block_add_provisioning_package.setter
    def settings_block_add_provisioning_package(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockAddProvisioningPackage property value. Indicates whether or not to block the user from installing provisioning packages.
        Args:
            value: Value to set for the settings_block_add_provisioning_package property.
        """
        self._settings_block_add_provisioning_package = value
    
    @property
    def settings_block_apps_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockAppsPage property value. Indicates whether or not to block access to Apps in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_apps_page
    
    @settings_block_apps_page.setter
    def settings_block_apps_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockAppsPage property value. Indicates whether or not to block access to Apps in Settings app.
        Args:
            value: Value to set for the settings_block_apps_page property.
        """
        self._settings_block_apps_page = value
    
    @property
    def settings_block_change_language(self,) -> Optional[bool]:
        """
        Gets the settingsBlockChangeLanguage property value. Indicates whether or not to block the user from changing the language settings.
        Returns: Optional[bool]
        """
        return self._settings_block_change_language
    
    @settings_block_change_language.setter
    def settings_block_change_language(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockChangeLanguage property value. Indicates whether or not to block the user from changing the language settings.
        Args:
            value: Value to set for the settings_block_change_language property.
        """
        self._settings_block_change_language = value
    
    @property
    def settings_block_change_power_sleep(self,) -> Optional[bool]:
        """
        Gets the settingsBlockChangePowerSleep property value. Indicates whether or not to block the user from changing power and sleep settings.
        Returns: Optional[bool]
        """
        return self._settings_block_change_power_sleep
    
    @settings_block_change_power_sleep.setter
    def settings_block_change_power_sleep(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockChangePowerSleep property value. Indicates whether or not to block the user from changing power and sleep settings.
        Args:
            value: Value to set for the settings_block_change_power_sleep property.
        """
        self._settings_block_change_power_sleep = value
    
    @property
    def settings_block_change_region(self,) -> Optional[bool]:
        """
        Gets the settingsBlockChangeRegion property value. Indicates whether or not to block the user from changing the region settings.
        Returns: Optional[bool]
        """
        return self._settings_block_change_region
    
    @settings_block_change_region.setter
    def settings_block_change_region(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockChangeRegion property value. Indicates whether or not to block the user from changing the region settings.
        Args:
            value: Value to set for the settings_block_change_region property.
        """
        self._settings_block_change_region = value
    
    @property
    def settings_block_change_system_time(self,) -> Optional[bool]:
        """
        Gets the settingsBlockChangeSystemTime property value. Indicates whether or not to block the user from changing date and time settings.
        Returns: Optional[bool]
        """
        return self._settings_block_change_system_time
    
    @settings_block_change_system_time.setter
    def settings_block_change_system_time(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockChangeSystemTime property value. Indicates whether or not to block the user from changing date and time settings.
        Args:
            value: Value to set for the settings_block_change_system_time property.
        """
        self._settings_block_change_system_time = value
    
    @property
    def settings_block_devices_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockDevicesPage property value. Indicates whether or not to block access to Devices in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_devices_page
    
    @settings_block_devices_page.setter
    def settings_block_devices_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockDevicesPage property value. Indicates whether or not to block access to Devices in Settings app.
        Args:
            value: Value to set for the settings_block_devices_page property.
        """
        self._settings_block_devices_page = value
    
    @property
    def settings_block_ease_of_access_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockEaseOfAccessPage property value. Indicates whether or not to block access to Ease of Access in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_ease_of_access_page
    
    @settings_block_ease_of_access_page.setter
    def settings_block_ease_of_access_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockEaseOfAccessPage property value. Indicates whether or not to block access to Ease of Access in Settings app.
        Args:
            value: Value to set for the settings_block_ease_of_access_page property.
        """
        self._settings_block_ease_of_access_page = value
    
    @property
    def settings_block_edit_device_name(self,) -> Optional[bool]:
        """
        Gets the settingsBlockEditDeviceName property value. Indicates whether or not to block the user from editing the device name.
        Returns: Optional[bool]
        """
        return self._settings_block_edit_device_name
    
    @settings_block_edit_device_name.setter
    def settings_block_edit_device_name(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockEditDeviceName property value. Indicates whether or not to block the user from editing the device name.
        Args:
            value: Value to set for the settings_block_edit_device_name property.
        """
        self._settings_block_edit_device_name = value
    
    @property
    def settings_block_gaming_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockGamingPage property value. Indicates whether or not to block access to Gaming in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_gaming_page
    
    @settings_block_gaming_page.setter
    def settings_block_gaming_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockGamingPage property value. Indicates whether or not to block access to Gaming in Settings app.
        Args:
            value: Value to set for the settings_block_gaming_page property.
        """
        self._settings_block_gaming_page = value
    
    @property
    def settings_block_network_internet_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockNetworkInternetPage property value. Indicates whether or not to block access to Network & Internet in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_network_internet_page
    
    @settings_block_network_internet_page.setter
    def settings_block_network_internet_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockNetworkInternetPage property value. Indicates whether or not to block access to Network & Internet in Settings app.
        Args:
            value: Value to set for the settings_block_network_internet_page property.
        """
        self._settings_block_network_internet_page = value
    
    @property
    def settings_block_personalization_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockPersonalizationPage property value. Indicates whether or not to block access to Personalization in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_personalization_page
    
    @settings_block_personalization_page.setter
    def settings_block_personalization_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockPersonalizationPage property value. Indicates whether or not to block access to Personalization in Settings app.
        Args:
            value: Value to set for the settings_block_personalization_page property.
        """
        self._settings_block_personalization_page = value
    
    @property
    def settings_block_privacy_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockPrivacyPage property value. Indicates whether or not to block access to Privacy in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_privacy_page
    
    @settings_block_privacy_page.setter
    def settings_block_privacy_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockPrivacyPage property value. Indicates whether or not to block access to Privacy in Settings app.
        Args:
            value: Value to set for the settings_block_privacy_page property.
        """
        self._settings_block_privacy_page = value
    
    @property
    def settings_block_remove_provisioning_package(self,) -> Optional[bool]:
        """
        Gets the settingsBlockRemoveProvisioningPackage property value. Indicates whether or not to block the runtime configuration agent from removing provisioning packages.
        Returns: Optional[bool]
        """
        return self._settings_block_remove_provisioning_package
    
    @settings_block_remove_provisioning_package.setter
    def settings_block_remove_provisioning_package(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockRemoveProvisioningPackage property value. Indicates whether or not to block the runtime configuration agent from removing provisioning packages.
        Args:
            value: Value to set for the settings_block_remove_provisioning_package property.
        """
        self._settings_block_remove_provisioning_package = value
    
    @property
    def settings_block_settings_app(self,) -> Optional[bool]:
        """
        Gets the settingsBlockSettingsApp property value. Indicates whether or not to block access to Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_settings_app
    
    @settings_block_settings_app.setter
    def settings_block_settings_app(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockSettingsApp property value. Indicates whether or not to block access to Settings app.
        Args:
            value: Value to set for the settings_block_settings_app property.
        """
        self._settings_block_settings_app = value
    
    @property
    def settings_block_system_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockSystemPage property value. Indicates whether or not to block access to System in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_system_page
    
    @settings_block_system_page.setter
    def settings_block_system_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockSystemPage property value. Indicates whether or not to block access to System in Settings app.
        Args:
            value: Value to set for the settings_block_system_page property.
        """
        self._settings_block_system_page = value
    
    @property
    def settings_block_time_language_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockTimeLanguagePage property value. Indicates whether or not to block access to Time & Language in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_time_language_page
    
    @settings_block_time_language_page.setter
    def settings_block_time_language_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockTimeLanguagePage property value. Indicates whether or not to block access to Time & Language in Settings app.
        Args:
            value: Value to set for the settings_block_time_language_page property.
        """
        self._settings_block_time_language_page = value
    
    @property
    def settings_block_update_security_page(self,) -> Optional[bool]:
        """
        Gets the settingsBlockUpdateSecurityPage property value. Indicates whether or not to block access to Update & Security in Settings app.
        Returns: Optional[bool]
        """
        return self._settings_block_update_security_page
    
    @settings_block_update_security_page.setter
    def settings_block_update_security_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockUpdateSecurityPage property value. Indicates whether or not to block access to Update & Security in Settings app.
        Args:
            value: Value to set for the settings_block_update_security_page property.
        """
        self._settings_block_update_security_page = value
    
    @property
    def shared_user_app_data_allowed(self,) -> Optional[bool]:
        """
        Gets the sharedUserAppDataAllowed property value. Indicates whether or not to block multiple users of the same app to share data.
        Returns: Optional[bool]
        """
        return self._shared_user_app_data_allowed
    
    @shared_user_app_data_allowed.setter
    def shared_user_app_data_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the sharedUserAppDataAllowed property value. Indicates whether or not to block multiple users of the same app to share data.
        Args:
            value: Value to set for the shared_user_app_data_allowed property.
        """
        self._shared_user_app_data_allowed = value
    
    @property
    def smart_screen_block_prompt_override(self,) -> Optional[bool]:
        """
        Gets the smartScreenBlockPromptOverride property value. Indicates whether or not users can override SmartScreen Filter warnings about potentially malicious websites.
        Returns: Optional[bool]
        """
        return self._smart_screen_block_prompt_override
    
    @smart_screen_block_prompt_override.setter
    def smart_screen_block_prompt_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenBlockPromptOverride property value. Indicates whether or not users can override SmartScreen Filter warnings about potentially malicious websites.
        Args:
            value: Value to set for the smart_screen_block_prompt_override property.
        """
        self._smart_screen_block_prompt_override = value
    
    @property
    def smart_screen_block_prompt_override_for_files(self,) -> Optional[bool]:
        """
        Gets the smartScreenBlockPromptOverrideForFiles property value. Indicates whether or not users can override the SmartScreen Filter warnings about downloading unverified files
        Returns: Optional[bool]
        """
        return self._smart_screen_block_prompt_override_for_files
    
    @smart_screen_block_prompt_override_for_files.setter
    def smart_screen_block_prompt_override_for_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenBlockPromptOverrideForFiles property value. Indicates whether or not users can override the SmartScreen Filter warnings about downloading unverified files
        Args:
            value: Value to set for the smart_screen_block_prompt_override_for_files property.
        """
        self._smart_screen_block_prompt_override_for_files = value
    
    @property
    def smart_screen_enable_app_install_control(self,) -> Optional[bool]:
        """
        Gets the smartScreenEnableAppInstallControl property value. This property will be deprecated in July 2019 and will be replaced by property SmartScreenAppInstallControl. Allows IT Admins to control whether users are allowed to install apps from places other than the Store.
        Returns: Optional[bool]
        """
        return self._smart_screen_enable_app_install_control
    
    @smart_screen_enable_app_install_control.setter
    def smart_screen_enable_app_install_control(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenEnableAppInstallControl property value. This property will be deprecated in July 2019 and will be replaced by property SmartScreenAppInstallControl. Allows IT Admins to control whether users are allowed to install apps from places other than the Store.
        Args:
            value: Value to set for the smart_screen_enable_app_install_control property.
        """
        self._smart_screen_enable_app_install_control = value
    
    @property
    def start_block_unpinning_apps_from_taskbar(self,) -> Optional[bool]:
        """
        Gets the startBlockUnpinningAppsFromTaskbar property value. Indicates whether or not to block the user from unpinning apps from taskbar.
        Returns: Optional[bool]
        """
        return self._start_block_unpinning_apps_from_taskbar
    
    @start_block_unpinning_apps_from_taskbar.setter
    def start_block_unpinning_apps_from_taskbar(self,value: Optional[bool] = None) -> None:
        """
        Sets the startBlockUnpinningAppsFromTaskbar property value. Indicates whether or not to block the user from unpinning apps from taskbar.
        Args:
            value: Value to set for the start_block_unpinning_apps_from_taskbar property.
        """
        self._start_block_unpinning_apps_from_taskbar = value
    
    @property
    def start_menu_app_list_visibility(self,) -> Optional[windows_start_menu_app_list_visibility_type.WindowsStartMenuAppListVisibilityType]:
        """
        Gets the startMenuAppListVisibility property value. Type of start menu app list visibility.
        Returns: Optional[windows_start_menu_app_list_visibility_type.WindowsStartMenuAppListVisibilityType]
        """
        return self._start_menu_app_list_visibility
    
    @start_menu_app_list_visibility.setter
    def start_menu_app_list_visibility(self,value: Optional[windows_start_menu_app_list_visibility_type.WindowsStartMenuAppListVisibilityType] = None) -> None:
        """
        Sets the startMenuAppListVisibility property value. Type of start menu app list visibility.
        Args:
            value: Value to set for the start_menu_app_list_visibility property.
        """
        self._start_menu_app_list_visibility = value
    
    @property
    def start_menu_hide_change_account_settings(self,) -> Optional[bool]:
        """
        Gets the startMenuHideChangeAccountSettings property value. Enabling this policy hides the change account setting from appearing in the user tile in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_change_account_settings
    
    @start_menu_hide_change_account_settings.setter
    def start_menu_hide_change_account_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideChangeAccountSettings property value. Enabling this policy hides the change account setting from appearing in the user tile in the start menu.
        Args:
            value: Value to set for the start_menu_hide_change_account_settings property.
        """
        self._start_menu_hide_change_account_settings = value
    
    @property
    def start_menu_hide_frequently_used_apps(self,) -> Optional[bool]:
        """
        Gets the startMenuHideFrequentlyUsedApps property value. Enabling this policy hides the most used apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_frequently_used_apps
    
    @start_menu_hide_frequently_used_apps.setter
    def start_menu_hide_frequently_used_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideFrequentlyUsedApps property value. Enabling this policy hides the most used apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
        Args:
            value: Value to set for the start_menu_hide_frequently_used_apps property.
        """
        self._start_menu_hide_frequently_used_apps = value
    
    @property
    def start_menu_hide_hibernate(self,) -> Optional[bool]:
        """
        Gets the startMenuHideHibernate property value. Enabling this policy hides hibernate from appearing in the power button in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_hibernate
    
    @start_menu_hide_hibernate.setter
    def start_menu_hide_hibernate(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideHibernate property value. Enabling this policy hides hibernate from appearing in the power button in the start menu.
        Args:
            value: Value to set for the start_menu_hide_hibernate property.
        """
        self._start_menu_hide_hibernate = value
    
    @property
    def start_menu_hide_lock(self,) -> Optional[bool]:
        """
        Gets the startMenuHideLock property value. Enabling this policy hides lock from appearing in the user tile in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_lock
    
    @start_menu_hide_lock.setter
    def start_menu_hide_lock(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideLock property value. Enabling this policy hides lock from appearing in the user tile in the start menu.
        Args:
            value: Value to set for the start_menu_hide_lock property.
        """
        self._start_menu_hide_lock = value
    
    @property
    def start_menu_hide_power_button(self,) -> Optional[bool]:
        """
        Gets the startMenuHidePowerButton property value. Enabling this policy hides the power button from appearing in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_power_button
    
    @start_menu_hide_power_button.setter
    def start_menu_hide_power_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHidePowerButton property value. Enabling this policy hides the power button from appearing in the start menu.
        Args:
            value: Value to set for the start_menu_hide_power_button property.
        """
        self._start_menu_hide_power_button = value
    
    @property
    def start_menu_hide_recent_jump_lists(self,) -> Optional[bool]:
        """
        Gets the startMenuHideRecentJumpLists property value. Enabling this policy hides recent jump lists from appearing on the start menu/taskbar and disables the corresponding toggle in the Settings app.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_recent_jump_lists
    
    @start_menu_hide_recent_jump_lists.setter
    def start_menu_hide_recent_jump_lists(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideRecentJumpLists property value. Enabling this policy hides recent jump lists from appearing on the start menu/taskbar and disables the corresponding toggle in the Settings app.
        Args:
            value: Value to set for the start_menu_hide_recent_jump_lists property.
        """
        self._start_menu_hide_recent_jump_lists = value
    
    @property
    def start_menu_hide_recently_added_apps(self,) -> Optional[bool]:
        """
        Gets the startMenuHideRecentlyAddedApps property value. Enabling this policy hides recently added apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_recently_added_apps
    
    @start_menu_hide_recently_added_apps.setter
    def start_menu_hide_recently_added_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideRecentlyAddedApps property value. Enabling this policy hides recently added apps from appearing on the start menu and disables the corresponding toggle in the Settings app.
        Args:
            value: Value to set for the start_menu_hide_recently_added_apps property.
        """
        self._start_menu_hide_recently_added_apps = value
    
    @property
    def start_menu_hide_restart_options(self,) -> Optional[bool]:
        """
        Gets the startMenuHideRestartOptions property value. Enabling this policy hides 'Restart/Update and Restart' from appearing in the power button in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_restart_options
    
    @start_menu_hide_restart_options.setter
    def start_menu_hide_restart_options(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideRestartOptions property value. Enabling this policy hides 'Restart/Update and Restart' from appearing in the power button in the start menu.
        Args:
            value: Value to set for the start_menu_hide_restart_options property.
        """
        self._start_menu_hide_restart_options = value
    
    @property
    def start_menu_hide_shut_down(self,) -> Optional[bool]:
        """
        Gets the startMenuHideShutDown property value. Enabling this policy hides shut down/update and shut down from appearing in the power button in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_shut_down
    
    @start_menu_hide_shut_down.setter
    def start_menu_hide_shut_down(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideShutDown property value. Enabling this policy hides shut down/update and shut down from appearing in the power button in the start menu.
        Args:
            value: Value to set for the start_menu_hide_shut_down property.
        """
        self._start_menu_hide_shut_down = value
    
    @property
    def start_menu_hide_sign_out(self,) -> Optional[bool]:
        """
        Gets the startMenuHideSignOut property value. Enabling this policy hides sign out from appearing in the user tile in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_sign_out
    
    @start_menu_hide_sign_out.setter
    def start_menu_hide_sign_out(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideSignOut property value. Enabling this policy hides sign out from appearing in the user tile in the start menu.
        Args:
            value: Value to set for the start_menu_hide_sign_out property.
        """
        self._start_menu_hide_sign_out = value
    
    @property
    def start_menu_hide_sleep(self,) -> Optional[bool]:
        """
        Gets the startMenuHideSleep property value. Enabling this policy hides sleep from appearing in the power button in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_sleep
    
    @start_menu_hide_sleep.setter
    def start_menu_hide_sleep(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideSleep property value. Enabling this policy hides sleep from appearing in the power button in the start menu.
        Args:
            value: Value to set for the start_menu_hide_sleep property.
        """
        self._start_menu_hide_sleep = value
    
    @property
    def start_menu_hide_switch_account(self,) -> Optional[bool]:
        """
        Gets the startMenuHideSwitchAccount property value. Enabling this policy hides switch account from appearing in the user tile in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_switch_account
    
    @start_menu_hide_switch_account.setter
    def start_menu_hide_switch_account(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideSwitchAccount property value. Enabling this policy hides switch account from appearing in the user tile in the start menu.
        Args:
            value: Value to set for the start_menu_hide_switch_account property.
        """
        self._start_menu_hide_switch_account = value
    
    @property
    def start_menu_hide_user_tile(self,) -> Optional[bool]:
        """
        Gets the startMenuHideUserTile property value. Enabling this policy hides the user tile from appearing in the start menu.
        Returns: Optional[bool]
        """
        return self._start_menu_hide_user_tile
    
    @start_menu_hide_user_tile.setter
    def start_menu_hide_user_tile(self,value: Optional[bool] = None) -> None:
        """
        Sets the startMenuHideUserTile property value. Enabling this policy hides the user tile from appearing in the start menu.
        Args:
            value: Value to set for the start_menu_hide_user_tile property.
        """
        self._start_menu_hide_user_tile = value
    
    @property
    def start_menu_layout_edge_assets_xml(self,) -> Optional[bytes]:
        """
        Gets the startMenuLayoutEdgeAssetsXml property value. This policy setting allows you to import Edge assets to be used with startMenuLayoutXml policy. Start layout can contain secondary tile from Edge app which looks for Edge local asset file. Edge local asset would not exist and cause Edge secondary tile to appear empty in this case. This policy only gets applied when startMenuLayoutXml policy is modified. The value should be a UTF-8 Base64 encoded byte array.
        Returns: Optional[bytes]
        """
        return self._start_menu_layout_edge_assets_xml
    
    @start_menu_layout_edge_assets_xml.setter
    def start_menu_layout_edge_assets_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the startMenuLayoutEdgeAssetsXml property value. This policy setting allows you to import Edge assets to be used with startMenuLayoutXml policy. Start layout can contain secondary tile from Edge app which looks for Edge local asset file. Edge local asset would not exist and cause Edge secondary tile to appear empty in this case. This policy only gets applied when startMenuLayoutXml policy is modified. The value should be a UTF-8 Base64 encoded byte array.
        Args:
            value: Value to set for the start_menu_layout_edge_assets_xml property.
        """
        self._start_menu_layout_edge_assets_xml = value
    
    @property
    def start_menu_layout_xml(self,) -> Optional[bytes]:
        """
        Gets the startMenuLayoutXml property value. Allows admins to override the default Start menu layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in a UTF8 encoded byte array format.
        Returns: Optional[bytes]
        """
        return self._start_menu_layout_xml
    
    @start_menu_layout_xml.setter
    def start_menu_layout_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the startMenuLayoutXml property value. Allows admins to override the default Start menu layout and prevents the user from changing it. The layout is modified by specifying an XML file based on a layout modification schema. XML needs to be in a UTF8 encoded byte array format.
        Args:
            value: Value to set for the start_menu_layout_xml property.
        """
        self._start_menu_layout_xml = value
    
    @property
    def start_menu_mode(self,) -> Optional[windows_start_menu_mode_type.WindowsStartMenuModeType]:
        """
        Gets the startMenuMode property value. Type of display modes for the start menu.
        Returns: Optional[windows_start_menu_mode_type.WindowsStartMenuModeType]
        """
        return self._start_menu_mode
    
    @start_menu_mode.setter
    def start_menu_mode(self,value: Optional[windows_start_menu_mode_type.WindowsStartMenuModeType] = None) -> None:
        """
        Sets the startMenuMode property value. Type of display modes for the start menu.
        Args:
            value: Value to set for the start_menu_mode property.
        """
        self._start_menu_mode = value
    
    @property
    def start_menu_pinned_folder_documents(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderDocuments property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_documents
    
    @start_menu_pinned_folder_documents.setter
    def start_menu_pinned_folder_documents(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderDocuments property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_documents property.
        """
        self._start_menu_pinned_folder_documents = value
    
    @property
    def start_menu_pinned_folder_downloads(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderDownloads property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_downloads
    
    @start_menu_pinned_folder_downloads.setter
    def start_menu_pinned_folder_downloads(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderDownloads property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_downloads property.
        """
        self._start_menu_pinned_folder_downloads = value
    
    @property
    def start_menu_pinned_folder_file_explorer(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderFileExplorer property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_file_explorer
    
    @start_menu_pinned_folder_file_explorer.setter
    def start_menu_pinned_folder_file_explorer(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderFileExplorer property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_file_explorer property.
        """
        self._start_menu_pinned_folder_file_explorer = value
    
    @property
    def start_menu_pinned_folder_home_group(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderHomeGroup property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_home_group
    
    @start_menu_pinned_folder_home_group.setter
    def start_menu_pinned_folder_home_group(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderHomeGroup property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_home_group property.
        """
        self._start_menu_pinned_folder_home_group = value
    
    @property
    def start_menu_pinned_folder_music(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderMusic property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_music
    
    @start_menu_pinned_folder_music.setter
    def start_menu_pinned_folder_music(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderMusic property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_music property.
        """
        self._start_menu_pinned_folder_music = value
    
    @property
    def start_menu_pinned_folder_network(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderNetwork property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_network
    
    @start_menu_pinned_folder_network.setter
    def start_menu_pinned_folder_network(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderNetwork property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_network property.
        """
        self._start_menu_pinned_folder_network = value
    
    @property
    def start_menu_pinned_folder_personal_folder(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderPersonalFolder property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_personal_folder
    
    @start_menu_pinned_folder_personal_folder.setter
    def start_menu_pinned_folder_personal_folder(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderPersonalFolder property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_personal_folder property.
        """
        self._start_menu_pinned_folder_personal_folder = value
    
    @property
    def start_menu_pinned_folder_pictures(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderPictures property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_pictures
    
    @start_menu_pinned_folder_pictures.setter
    def start_menu_pinned_folder_pictures(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderPictures property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_pictures property.
        """
        self._start_menu_pinned_folder_pictures = value
    
    @property
    def start_menu_pinned_folder_settings(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderSettings property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_settings
    
    @start_menu_pinned_folder_settings.setter
    def start_menu_pinned_folder_settings(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderSettings property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_settings property.
        """
        self._start_menu_pinned_folder_settings = value
    
    @property
    def start_menu_pinned_folder_videos(self,) -> Optional[visibility_setting.VisibilitySetting]:
        """
        Gets the startMenuPinnedFolderVideos property value. Generic visibility state.
        Returns: Optional[visibility_setting.VisibilitySetting]
        """
        return self._start_menu_pinned_folder_videos
    
    @start_menu_pinned_folder_videos.setter
    def start_menu_pinned_folder_videos(self,value: Optional[visibility_setting.VisibilitySetting] = None) -> None:
        """
        Sets the startMenuPinnedFolderVideos property value. Generic visibility state.
        Args:
            value: Value to set for the start_menu_pinned_folder_videos property.
        """
        self._start_menu_pinned_folder_videos = value
    
    @property
    def storage_block_removable_storage(self,) -> Optional[bool]:
        """
        Gets the storageBlockRemovableStorage property value. Indicates whether or not to Block the user from using removable storage.
        Returns: Optional[bool]
        """
        return self._storage_block_removable_storage
    
    @storage_block_removable_storage.setter
    def storage_block_removable_storage(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockRemovableStorage property value. Indicates whether or not to Block the user from using removable storage.
        Args:
            value: Value to set for the storage_block_removable_storage property.
        """
        self._storage_block_removable_storage = value
    
    @property
    def storage_require_mobile_device_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireMobileDeviceEncryption property value. Indicating whether or not to require encryption on a mobile device.
        Returns: Optional[bool]
        """
        return self._storage_require_mobile_device_encryption
    
    @storage_require_mobile_device_encryption.setter
    def storage_require_mobile_device_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireMobileDeviceEncryption property value. Indicating whether or not to require encryption on a mobile device.
        Args:
            value: Value to set for the storage_require_mobile_device_encryption property.
        """
        self._storage_require_mobile_device_encryption = value
    
    @property
    def storage_restrict_app_data_to_system_volume(self,) -> Optional[bool]:
        """
        Gets the storageRestrictAppDataToSystemVolume property value. Indicates whether application data is restricted to the system drive.
        Returns: Optional[bool]
        """
        return self._storage_restrict_app_data_to_system_volume
    
    @storage_restrict_app_data_to_system_volume.setter
    def storage_restrict_app_data_to_system_volume(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRestrictAppDataToSystemVolume property value. Indicates whether application data is restricted to the system drive.
        Args:
            value: Value to set for the storage_restrict_app_data_to_system_volume property.
        """
        self._storage_restrict_app_data_to_system_volume = value
    
    @property
    def storage_restrict_app_install_to_system_volume(self,) -> Optional[bool]:
        """
        Gets the storageRestrictAppInstallToSystemVolume property value. Indicates whether the installation of applications is restricted to the system drive.
        Returns: Optional[bool]
        """
        return self._storage_restrict_app_install_to_system_volume
    
    @storage_restrict_app_install_to_system_volume.setter
    def storage_restrict_app_install_to_system_volume(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRestrictAppInstallToSystemVolume property value. Indicates whether the installation of applications is restricted to the system drive.
        Args:
            value: Value to set for the storage_restrict_app_install_to_system_volume property.
        """
        self._storage_restrict_app_install_to_system_volume = value
    
    @property
    def tenant_lockdown_require_network_during_out_of_box_experience(self,) -> Optional[bool]:
        """
        Gets the tenantLockdownRequireNetworkDuringOutOfBoxExperience property value. Whether the device is required to connect to the network.
        Returns: Optional[bool]
        """
        return self._tenant_lockdown_require_network_during_out_of_box_experience
    
    @tenant_lockdown_require_network_during_out_of_box_experience.setter
    def tenant_lockdown_require_network_during_out_of_box_experience(self,value: Optional[bool] = None) -> None:
        """
        Sets the tenantLockdownRequireNetworkDuringOutOfBoxExperience property value. Whether the device is required to connect to the network.
        Args:
            value: Value to set for the tenant_lockdown_require_network_during_out_of_box_experience property.
        """
        self._tenant_lockdown_require_network_during_out_of_box_experience = value
    
    @property
    def usb_blocked(self,) -> Optional[bool]:
        """
        Gets the usbBlocked property value. Indicates whether or not to Block the user from USB connection.
        Returns: Optional[bool]
        """
        return self._usb_blocked
    
    @usb_blocked.setter
    def usb_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the usbBlocked property value. Indicates whether or not to Block the user from USB connection.
        Args:
            value: Value to set for the usb_blocked property.
        """
        self._usb_blocked = value
    
    @property
    def voice_recording_blocked(self,) -> Optional[bool]:
        """
        Gets the voiceRecordingBlocked property value. Indicates whether or not to Block the user from voice recording.
        Returns: Optional[bool]
        """
        return self._voice_recording_blocked
    
    @voice_recording_blocked.setter
    def voice_recording_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the voiceRecordingBlocked property value. Indicates whether or not to Block the user from voice recording.
        Args:
            value: Value to set for the voice_recording_blocked property.
        """
        self._voice_recording_blocked = value
    
    @property
    def web_rtc_block_localhost_ip_address(self,) -> Optional[bool]:
        """
        Gets the webRtcBlockLocalhostIpAddress property value. Indicates whether or not user's localhost IP address is displayed while making phone calls using the WebRTC
        Returns: Optional[bool]
        """
        return self._web_rtc_block_localhost_ip_address
    
    @web_rtc_block_localhost_ip_address.setter
    def web_rtc_block_localhost_ip_address(self,value: Optional[bool] = None) -> None:
        """
        Sets the webRtcBlockLocalhostIpAddress property value. Indicates whether or not user's localhost IP address is displayed while making phone calls using the WebRTC
        Args:
            value: Value to set for the web_rtc_block_localhost_ip_address property.
        """
        self._web_rtc_block_localhost_ip_address = value
    
    @property
    def wi_fi_block_automatic_connect_hotspots(self,) -> Optional[bool]:
        """
        Gets the wiFiBlockAutomaticConnectHotspots property value. Indicating whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
        Returns: Optional[bool]
        """
        return self._wi_fi_block_automatic_connect_hotspots
    
    @wi_fi_block_automatic_connect_hotspots.setter
    def wi_fi_block_automatic_connect_hotspots(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiBlockAutomaticConnectHotspots property value. Indicating whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
        Args:
            value: Value to set for the wi_fi_block_automatic_connect_hotspots property.
        """
        self._wi_fi_block_automatic_connect_hotspots = value
    
    @property
    def wi_fi_block_manual_configuration(self,) -> Optional[bool]:
        """
        Gets the wiFiBlockManualConfiguration property value. Indicates whether or not to Block the user from using Wi-Fi manual configuration.
        Returns: Optional[bool]
        """
        return self._wi_fi_block_manual_configuration
    
    @wi_fi_block_manual_configuration.setter
    def wi_fi_block_manual_configuration(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiBlockManualConfiguration property value. Indicates whether or not to Block the user from using Wi-Fi manual configuration.
        Args:
            value: Value to set for the wi_fi_block_manual_configuration property.
        """
        self._wi_fi_block_manual_configuration = value
    
    @property
    def wi_fi_blocked(self,) -> Optional[bool]:
        """
        Gets the wiFiBlocked property value. Indicates whether or not to Block the user from using Wi-Fi.
        Returns: Optional[bool]
        """
        return self._wi_fi_blocked
    
    @wi_fi_blocked.setter
    def wi_fi_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiBlocked property value. Indicates whether or not to Block the user from using Wi-Fi.
        Args:
            value: Value to set for the wi_fi_blocked property.
        """
        self._wi_fi_blocked = value
    
    @property
    def wi_fi_scan_interval(self,) -> Optional[int]:
        """
        Gets the wiFiScanInterval property value. Specify how often devices scan for Wi-Fi networks. Supported values are 1-500, where 100 = default, and 500 = low frequency. Valid values 1 to 500
        Returns: Optional[int]
        """
        return self._wi_fi_scan_interval
    
    @wi_fi_scan_interval.setter
    def wi_fi_scan_interval(self,value: Optional[int] = None) -> None:
        """
        Sets the wiFiScanInterval property value. Specify how often devices scan for Wi-Fi networks. Supported values are 1-500, where 100 = default, and 500 = low frequency. Valid values 1 to 500
        Args:
            value: Value to set for the wi_fi_scan_interval property.
        """
        self._wi_fi_scan_interval = value
    
    @property
    def windows_spotlight_block_consumer_specific_features(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlockConsumerSpecificFeatures property value. Allows IT admins to block experiences that are typically for consumers only, such as Start suggestions, Membership notifications, Post-OOBE app install and redirect tiles.
        Returns: Optional[bool]
        """
        return self._windows_spotlight_block_consumer_specific_features
    
    @windows_spotlight_block_consumer_specific_features.setter
    def windows_spotlight_block_consumer_specific_features(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlockConsumerSpecificFeatures property value. Allows IT admins to block experiences that are typically for consumers only, such as Start suggestions, Membership notifications, Post-OOBE app install and redirect tiles.
        Args:
            value: Value to set for the windows_spotlight_block_consumer_specific_features property.
        """
        self._windows_spotlight_block_consumer_specific_features = value
    
    @property
    def windows_spotlight_block_on_action_center(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlockOnActionCenter property value. Block suggestions from Microsoft that show after each OS clean install, upgrade or in an on-going basis to introduce users to what is new or changed
        Returns: Optional[bool]
        """
        return self._windows_spotlight_block_on_action_center
    
    @windows_spotlight_block_on_action_center.setter
    def windows_spotlight_block_on_action_center(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlockOnActionCenter property value. Block suggestions from Microsoft that show after each OS clean install, upgrade or in an on-going basis to introduce users to what is new or changed
        Args:
            value: Value to set for the windows_spotlight_block_on_action_center property.
        """
        self._windows_spotlight_block_on_action_center = value
    
    @property
    def windows_spotlight_block_tailored_experiences(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlockTailoredExperiences property value. Block personalized content in Windows spotlight based on user’s device usage.
        Returns: Optional[bool]
        """
        return self._windows_spotlight_block_tailored_experiences
    
    @windows_spotlight_block_tailored_experiences.setter
    def windows_spotlight_block_tailored_experiences(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlockTailoredExperiences property value. Block personalized content in Windows spotlight based on user’s device usage.
        Args:
            value: Value to set for the windows_spotlight_block_tailored_experiences property.
        """
        self._windows_spotlight_block_tailored_experiences = value
    
    @property
    def windows_spotlight_block_third_party_notifications(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlockThirdPartyNotifications property value. Block third party content delivered via Windows Spotlight
        Returns: Optional[bool]
        """
        return self._windows_spotlight_block_third_party_notifications
    
    @windows_spotlight_block_third_party_notifications.setter
    def windows_spotlight_block_third_party_notifications(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlockThirdPartyNotifications property value. Block third party content delivered via Windows Spotlight
        Args:
            value: Value to set for the windows_spotlight_block_third_party_notifications property.
        """
        self._windows_spotlight_block_third_party_notifications = value
    
    @property
    def windows_spotlight_block_welcome_experience(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlockWelcomeExperience property value. Block Windows Spotlight Windows welcome experience
        Returns: Optional[bool]
        """
        return self._windows_spotlight_block_welcome_experience
    
    @windows_spotlight_block_welcome_experience.setter
    def windows_spotlight_block_welcome_experience(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlockWelcomeExperience property value. Block Windows Spotlight Windows welcome experience
        Args:
            value: Value to set for the windows_spotlight_block_welcome_experience property.
        """
        self._windows_spotlight_block_welcome_experience = value
    
    @property
    def windows_spotlight_block_windows_tips(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlockWindowsTips property value. Allows IT admins to turn off the popup of Windows Tips.
        Returns: Optional[bool]
        """
        return self._windows_spotlight_block_windows_tips
    
    @windows_spotlight_block_windows_tips.setter
    def windows_spotlight_block_windows_tips(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlockWindowsTips property value. Allows IT admins to turn off the popup of Windows Tips.
        Args:
            value: Value to set for the windows_spotlight_block_windows_tips property.
        """
        self._windows_spotlight_block_windows_tips = value
    
    @property
    def windows_spotlight_blocked(self,) -> Optional[bool]:
        """
        Gets the windowsSpotlightBlocked property value. Allows IT admins to turn off all Windows Spotlight features
        Returns: Optional[bool]
        """
        return self._windows_spotlight_blocked
    
    @windows_spotlight_blocked.setter
    def windows_spotlight_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsSpotlightBlocked property value. Allows IT admins to turn off all Windows Spotlight features
        Args:
            value: Value to set for the windows_spotlight_blocked property.
        """
        self._windows_spotlight_blocked = value
    
    @property
    def windows_spotlight_configure_on_lock_screen(self,) -> Optional[windows_spotlight_enablement_settings.WindowsSpotlightEnablementSettings]:
        """
        Gets the windowsSpotlightConfigureOnLockScreen property value. Allows IT admind to set a predefined default search engine for MDM-Controlled devices
        Returns: Optional[windows_spotlight_enablement_settings.WindowsSpotlightEnablementSettings]
        """
        return self._windows_spotlight_configure_on_lock_screen
    
    @windows_spotlight_configure_on_lock_screen.setter
    def windows_spotlight_configure_on_lock_screen(self,value: Optional[windows_spotlight_enablement_settings.WindowsSpotlightEnablementSettings] = None) -> None:
        """
        Sets the windowsSpotlightConfigureOnLockScreen property value. Allows IT admind to set a predefined default search engine for MDM-Controlled devices
        Args:
            value: Value to set for the windows_spotlight_configure_on_lock_screen property.
        """
        self._windows_spotlight_configure_on_lock_screen = value
    
    @property
    def windows_store_block_auto_update(self,) -> Optional[bool]:
        """
        Gets the windowsStoreBlockAutoUpdate property value. Indicates whether or not to block automatic update of apps from Windows Store.
        Returns: Optional[bool]
        """
        return self._windows_store_block_auto_update
    
    @windows_store_block_auto_update.setter
    def windows_store_block_auto_update(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsStoreBlockAutoUpdate property value. Indicates whether or not to block automatic update of apps from Windows Store.
        Args:
            value: Value to set for the windows_store_block_auto_update property.
        """
        self._windows_store_block_auto_update = value
    
    @property
    def windows_store_blocked(self,) -> Optional[bool]:
        """
        Gets the windowsStoreBlocked property value. Indicates whether or not to Block the user from using the Windows store.
        Returns: Optional[bool]
        """
        return self._windows_store_blocked
    
    @windows_store_blocked.setter
    def windows_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsStoreBlocked property value. Indicates whether or not to Block the user from using the Windows store.
        Args:
            value: Value to set for the windows_store_blocked property.
        """
        self._windows_store_blocked = value
    
    @property
    def windows_store_enable_private_store_only(self,) -> Optional[bool]:
        """
        Gets the windowsStoreEnablePrivateStoreOnly property value. Indicates whether or not to enable Private Store Only.
        Returns: Optional[bool]
        """
        return self._windows_store_enable_private_store_only
    
    @windows_store_enable_private_store_only.setter
    def windows_store_enable_private_store_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsStoreEnablePrivateStoreOnly property value. Indicates whether or not to enable Private Store Only.
        Args:
            value: Value to set for the windows_store_enable_private_store_only property.
        """
        self._windows_store_enable_private_store_only = value
    
    @property
    def wireless_display_block_projection_to_this_device(self,) -> Optional[bool]:
        """
        Gets the wirelessDisplayBlockProjectionToThisDevice property value. Indicates whether or not to allow other devices from discovering this PC for projection.
        Returns: Optional[bool]
        """
        return self._wireless_display_block_projection_to_this_device
    
    @wireless_display_block_projection_to_this_device.setter
    def wireless_display_block_projection_to_this_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the wirelessDisplayBlockProjectionToThisDevice property value. Indicates whether or not to allow other devices from discovering this PC for projection.
        Args:
            value: Value to set for the wireless_display_block_projection_to_this_device property.
        """
        self._wireless_display_block_projection_to_this_device = value
    
    @property
    def wireless_display_block_user_input_from_receiver(self,) -> Optional[bool]:
        """
        Gets the wirelessDisplayBlockUserInputFromReceiver property value. Indicates whether or not to allow user input from wireless display receiver.
        Returns: Optional[bool]
        """
        return self._wireless_display_block_user_input_from_receiver
    
    @wireless_display_block_user_input_from_receiver.setter
    def wireless_display_block_user_input_from_receiver(self,value: Optional[bool] = None) -> None:
        """
        Sets the wirelessDisplayBlockUserInputFromReceiver property value. Indicates whether or not to allow user input from wireless display receiver.
        Args:
            value: Value to set for the wireless_display_block_user_input_from_receiver property.
        """
        self._wireless_display_block_user_input_from_receiver = value
    
    @property
    def wireless_display_require_pin_for_pairing(self,) -> Optional[bool]:
        """
        Gets the wirelessDisplayRequirePinForPairing property value. Indicates whether or not to require a PIN for new devices to initiate pairing.
        Returns: Optional[bool]
        """
        return self._wireless_display_require_pin_for_pairing
    
    @wireless_display_require_pin_for_pairing.setter
    def wireless_display_require_pin_for_pairing(self,value: Optional[bool] = None) -> None:
        """
        Sets the wirelessDisplayRequirePinForPairing property value. Indicates whether or not to require a PIN for new devices to initiate pairing.
        Args:
            value: Value to set for the wireless_display_require_pin_for_pairing property.
        """
        self._wireless_display_require_pin_for_pairing = value
    

