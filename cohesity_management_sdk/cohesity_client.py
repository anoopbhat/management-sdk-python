# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.decorators import lazy_property
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.controllers.alerts_controller import AlertsController
from cohesity_management_sdk.controllers.active_directory_controller import ActiveDirectoryController
from cohesity_management_sdk.controllers.tenant_controller import TenantController
from cohesity_management_sdk.controllers.static_route_controller import StaticRouteController
from cohesity_management_sdk.controllers.preferences_controller import PreferencesController
from cohesity_management_sdk.controllers.notifications_controller import NotificationsController
from cohesity_management_sdk.controllers.principals_controller import PrincipalsController
from cohesity_management_sdk.controllers.routes_controller import RoutesController
from cohesity_management_sdk.controllers.remote_cluster_controller import RemoteClusterController
from cohesity_management_sdk.controllers.nodes_controller import NodesController
from cohesity_management_sdk.controllers.interface_group_controller import InterfaceGroupController
from cohesity_management_sdk.controllers.clusters_controller import ClustersController
from cohesity_management_sdk.controllers.certificates_controller import CertificatesController
from cohesity_management_sdk.controllers.app_controller import AppController
from cohesity_management_sdk.controllers.app_instance_controller import AppInstanceController
from cohesity_management_sdk.controllers.vlan_controller import VlanController
from cohesity_management_sdk.controllers.views_controller import ViewsController
from cohesity_management_sdk.controllers.view_boxes_controller import ViewBoxesController
from cohesity_management_sdk.controllers.restore_tasks_controller import RestoreTasksController
from cohesity_management_sdk.controllers.vaults_controller import VaultsController
from cohesity_management_sdk.controllers.tenants_controller import TenantsController
from cohesity_management_sdk.controllers.statistics_controller import StatisticsController
from cohesity_management_sdk.controllers.smb_file_opens_controller import SMBFileOpensController
from cohesity_management_sdk.controllers.search_controller import SearchController
from cohesity_management_sdk.controllers.roles_controller import RolesController
from cohesity_management_sdk.controllers.remote_restore_controller import RemoteRestoreController
from cohesity_management_sdk.controllers.protection_sources_controller import ProtectionSourcesController
from cohesity_management_sdk.controllers.protection_runs_controller import ProtectionRunsController
from cohesity_management_sdk.controllers.protection_policies_controller import ProtectionPoliciesController
from cohesity_management_sdk.controllers.protection_jobs_controller import ProtectionJobsController
from cohesity_management_sdk.controllers.audit_controller import AuditController
from cohesity_management_sdk.controllers.kms_configuration_controller import KmsConfigurationController
from cohesity_management_sdk.controllers.privileges_controller import PrivilegesController
from cohesity_management_sdk.controllers.ldap_provider_controller import LdapProviderController
from cohesity_management_sdk.controllers.import_controller import ImportController
from cohesity_management_sdk.controllers.idps_controller import IdpsController
from cohesity_management_sdk.controllers.groups_controller import GroupsController
from cohesity_management_sdk.controllers.dashboard_controller import DashboardController
from cohesity_management_sdk.controllers.cluster_partitions_controller import ClusterPartitionsController
from cohesity_management_sdk.controllers.export_controller import ExportController
from cohesity_management_sdk.controllers.cluster_controller import ClusterController
from cohesity_management_sdk.controllers.access_tokens_controller import AccessTokensController


class CohesityClient(object):

    auth = AuthManager
    config = Configuration

    @lazy_property
    def alerts(self):
        return AlertsController()

    @lazy_property
    def active_directory(self):
        return ActiveDirectoryController()

    @lazy_property
    def tenant(self):
        return TenantController()

    @lazy_property
    def static_route(self):
        return StaticRouteController()

    @lazy_property
    def preferences(self):
        return PreferencesController()

    @lazy_property
    def notifications(self):
        return NotificationsController()

    @lazy_property
    def principals(self):
        return PrincipalsController()

    @lazy_property
    def routes(self):
        return RoutesController()

    @lazy_property
    def remote_cluster(self):
        return RemoteClusterController()

    @lazy_property
    def nodes(self):
        return NodesController()

    @lazy_property
    def interface_group(self):
        return InterfaceGroupController()

    @lazy_property
    def clusters(self):
        return ClustersController()

    @lazy_property
    def certificates(self):
        return CertificatesController()

    @lazy_property
    def app(self):
        return AppController()

    @lazy_property
    def app_instance(self):
        return AppInstanceController()

    @lazy_property
    def vlan(self):
        return VlanController()

    @lazy_property
    def views(self):
        return ViewsController()

    @lazy_property
    def view_boxes(self):
        return ViewBoxesController()

    @lazy_property
    def restore_tasks(self):
        return RestoreTasksController()

    @lazy_property
    def vaults(self):
        return VaultsController()

    @lazy_property
    def tenants(self):
        return TenantsController()

    @lazy_property
    def statistics(self):
        return StatisticsController()

    @lazy_property
    def smb_file_opens(self):
        return SMBFileOpensController()

    @lazy_property
    def search(self):
        return SearchController()

    @lazy_property
    def roles(self):
        return RolesController()

    @lazy_property
    def remote_restore(self):
        return RemoteRestoreController()

    @lazy_property
    def protection_sources(self):
        return ProtectionSourcesController()

    @lazy_property
    def protection_runs(self):
        return ProtectionRunsController()

    @lazy_property
    def protection_policies(self):
        return ProtectionPoliciesController()

    @lazy_property
    def protection_jobs(self):
        return ProtectionJobsController()

    @lazy_property
    def audit(self):
        return AuditController()

    @lazy_property
    def kms_configuration(self):
        return KmsConfigurationController()

    @lazy_property
    def privileges(self):
        return PrivilegesController()

    @lazy_property
    def ldap_provider(self):
        return LdapProviderController()

    @lazy_property
    def mimport(self):
        return ImportController()

    @lazy_property
    def idps(self):
        return IdpsController()

    @lazy_property
    def groups(self):
        return GroupsController()

    @lazy_property
    def dashboard(self):
        return DashboardController()

    @lazy_property
    def cluster_partitions(self):
        return ClusterPartitionsController()

    @lazy_property
    def export(self):
        return ExportController()

    @lazy_property
    def cluster(self):
        return ClusterController()

    @lazy_property
    def access_tokens(self):
        return AccessTokensController()

    def __init__(self,
                 cluster_vip=None,
                 username=None,
                 password=None,
                 domain=None,
                 auth_token=None):
        #CohesityPatch
        if cluster_vip == None:
            raise Exception("Specify cluster VIP")
        if auth_token != None:
            Configuration.auth_token = auth_token
        if username != None:
            Configuration.username = username
        if password != None:
            Configuration.password = password
            Configuration.auth_token = None  # Flushing existing token.
        if domain != None:
            Configuration.domain = domain
        Configuration.cluster_vip = cluster_vip
