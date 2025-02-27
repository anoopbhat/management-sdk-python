# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.universal_id
import cohesity_management_sdk.models.remote_protection_job_run_instance

class RemoteProtectionJobRunInformation(object):

    """Implementation of the 'RemoteProtectionJobRunInformation' model.

    Specifies details about a Protection Job Runs (Snapshots).

    Attributes:
        cluster_name (string): Specifies the name of the original Cluster that
            archived the data to the Vault.
        environment (EnvironmentRemoteProtectionJobRunInformationEnum):
            Specifies the environment type (such as kVMware or kSQL) of the
            original archived Protection Job. Supported environment types such
            as 'kView', 'kSQL', 'kVMware', etc. NOTE: 'kPuppeteer' refers to
            Cohesity's Remote Adapter. 'kVMware' indicates the VMware
            Protection Source environment. 'kHyperV' indicates the HyperV
            Protection Source environment. 'kSQL' indicates the SQL Protection
            Source environment. 'kView' indicates the View Protection Source
            environment. 'kPuppeteer' indicates the Cohesity's Remote Adapter.
            'kPhysical' indicates the physical Protection Source environment.
            'kPure' indicates the Pure Storage Protection Source environment.
            'kAzure' indicates the Microsoft's Azure Protection Source
            environment. 'kNetapp' indicates the Netapp Protection Source
            environment. 'kAgent' indicates the Agent Protection Source
            environment. 'kGenericNas' indicates the Genreric Network Attached
            Storage Protection Source environment. 'kAcropolis' indicates the
            Acropolis Protection Source environment. 'kPhsicalFiles' indicates
            the Physical Files Protection Source environment. 'kIsilon'
            indicates the Dell EMC's Isilon Protection Source environment.
            'kGPFS' indicates IBM's GPFS Protection Source environment. 'kKVM'
            indicates the KVM Protection Source environment. 'kAWS' indicates
            the AWS Protection Source environment. 'kExchange' indicates the
            Exchange Protection Source environment. 'kHyperVVSS' indicates the
            HyperV VSS Protection Source environment. 'kOracle' indicates the
            Oracle Protection Source environment. 'kGCP' indicates the Google
            Cloud Platform Protection Source environment. 'kFlashBlade'
            indicates the Flash Blade Protection Source environment.
            'kAWSNative' indicates the AWS Native Protection Source
            environment. 'kVCD' indicates the VMware's Virtual cloud Director
            Protection Source environment. 'kO365' indicates the Office 365
            Protection Source environment. 'kO365Outlook' indicates Office 365
            outlook Protection Source environment. 'kHyperFlex' indicates the
            Hyper Flex Protection Source environment. 'kGCPNative' indicates
            the GCP Native Protection Source environment. 'kAzureNative'
            indicates the Azure Native Protection Source environment.
            'kKubernetes' indicates a Kubernetes Protection Source
            environment.
        job_name (string): Specifies the name of the Protection Job on the
            original Cluster.
        job_uid (UniversalId): Specifies the globally unique id of the
            original Protection Job that archived the data to the Vault. This
            id is assigned by the original Cluster that archived the data.
        protection_job_runs (list of RemoteProtectionJobRunInstance): Array of
            Protection Job Run Details.  Specifies the list of Protection Job
            Runs (Snapshot) details for a Protection Job archived to a Vault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_name":'clusterName',
        "environment":'environment',
        "job_name":'jobName',
        "job_uid":'jobUid',
        "protection_job_runs":'protectionJobRuns'
    }

    def __init__(self,
                 cluster_name=None,
                 environment=None,
                 job_name=None,
                 job_uid=None,
                 protection_job_runs=None):
        """Constructor for the RemoteProtectionJobRunInformation class"""

        # Initialize members of the class
        self.cluster_name = cluster_name
        self.environment = environment
        self.job_name = job_name
        self.job_uid = job_uid
        self.protection_job_runs = protection_job_runs


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        cluster_name = dictionary.get('clusterName')
        environment = dictionary.get('environment')
        job_name = dictionary.get('jobName')
        job_uid = cohesity_management_sdk.models.universal_id.UniversalId.from_dictionary(dictionary.get('jobUid')) if dictionary.get('jobUid') else None
        protection_job_runs = None
        if dictionary.get('protectionJobRuns') != None:
            protection_job_runs = list()
            for structure in dictionary.get('protectionJobRuns'):
                protection_job_runs.append(cohesity_management_sdk.models.remote_protection_job_run_instance.RemoteProtectionJobRunInstance.from_dictionary(structure))

        # Return an object of this model
        return cls(cluster_name,
                   environment,
                   job_name,
                   job_uid,
                   protection_job_runs)


