# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.entity_permission_information
import cohesity_management_sdk.models.aggregated_subtree_info
import cohesity_management_sdk.models.protection_source
import cohesity_management_sdk.models.registered_source_info

class ProtectionSourceNode(object):

    """Implementation of the 'ProtectionSourceNode' model.

    Many different node types are supported such as
    'kComputeResource' and 'kResourcePool'.

    Attributes:
        application_nodes (list of object): Array of Child Subtrees.
            Specifies the child subtree used to store additional
            application-level Objects. Different environments use the subtree
            to store application-level information. For example for SQL
            Server, this subtree stores the SQL Server instances running on a
            VM.
        entity_permission_info (EntityPermissionInformation): Specifies the
            permission information of entities.
        logical_size (long|int): Specifies the logical size of the data in
            bytes for the Object on this node. Presence of this field
            indicates this node is a leaf node.
        nodes (list of object): Array of Child Nodes.  Specifies children of
            the current node in the Protection Sources hierarchy. When
            representing Objects in memory, the entire Object subtree
            hierarchy is represented. You can use this subtree to navigate
            down the Object hierarchy.
        protected_sources_summary (list of AggregatedSubtreeInfo): Array of
            Protected Objects.  Specifies aggregated information about all the
            child Objects of this node that are currently protected by a
            Protection Job. There is one entry for each environment that is
            being backed up. The aggregated information for the Object
            hierarchy's environment will be available at the 0th index of the
            vector.
        protection_source (ProtectionSource): Specifies the Protection Source
            for the current node.
        registration_info (RegisteredSourceInfo): Specifies registration
            information for a root node in a Protection Sources tree. A root
            node represents a registered Source on the Cohesity Cluster, such
            as a vCenter Server.
        unprotected_sources_summary (list of AggregatedSubtreeInfo): Array of
            Unprotected Sources.  Specifies aggregated information about all
            the child Objects of this node that are not protected by any
            Protection Jobs. The aggregated information for the Objects
            hierarchy's environment will be available at the 0th index of the
            vector. NOTE: This list includes Objects that were protected at
            some point in the past but are no longer actively protected.
            Snapshots containing these Objects may even exist on the Cohesity
            Cluster and be available to recover from.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_nodes":'applicationNodes',
        "entity_permission_info":'entityPermissionInfo',
        "logical_size":'logicalSize',
        "nodes":'nodes',
        "protected_sources_summary":'protectedSourcesSummary',
        "protection_source":'protectionSource',
        "registration_info":'registrationInfo',
        "unprotected_sources_summary":'unprotectedSourcesSummary'
    }

    def __init__(self,
                 application_nodes=None,
                 entity_permission_info=None,
                 logical_size=None,
                 nodes=None,
                 protected_sources_summary=None,
                 protection_source=None,
                 registration_info=None,
                 unprotected_sources_summary=None):
        """Constructor for the ProtectionSourceNode class"""

        # Initialize members of the class
        self.application_nodes = application_nodes
        self.entity_permission_info = entity_permission_info
        self.logical_size = logical_size
        self.nodes = nodes
        self.protected_sources_summary = protected_sources_summary
        self.protection_source = protection_source
        self.registration_info = registration_info
        self.unprotected_sources_summary = unprotected_sources_summary


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
        application_nodes = dictionary.get('applicationNodes')
        entity_permission_info = cohesity_management_sdk.models.entity_permission_information.EntityPermissionInformation.from_dictionary(dictionary.get('entityPermissionInfo')) if dictionary.get('entityPermissionInfo') else None
        logical_size = dictionary.get('logicalSize')
        nodes = dictionary.get('nodes')
        protected_sources_summary = None
        if dictionary.get('protectedSourcesSummary') != None:
            protected_sources_summary = list()
            for structure in dictionary.get('protectedSourcesSummary'):
                protected_sources_summary.append(cohesity_management_sdk.models.aggregated_subtree_info.AggregatedSubtreeInfo.from_dictionary(structure))
        protection_source = cohesity_management_sdk.models.protection_source.ProtectionSource.from_dictionary(dictionary.get('protectionSource')) if dictionary.get('protectionSource') else None
        registration_info = cohesity_management_sdk.models.registered_source_info.RegisteredSourceInfo.from_dictionary(dictionary.get('registrationInfo')) if dictionary.get('registrationInfo') else None
        unprotected_sources_summary = None
        if dictionary.get('unprotectedSourcesSummary') != None:
            unprotected_sources_summary = list()
            for structure in dictionary.get('unprotectedSourcesSummary'):
                unprotected_sources_summary.append(cohesity_management_sdk.models.aggregated_subtree_info.AggregatedSubtreeInfo.from_dictionary(structure))

        # Return an object of this model
        return cls(application_nodes,
                   entity_permission_info,
                   logical_size,
                   nodes,
                   protected_sources_summary,
                   protection_source,
                   registration_info,
                   unprotected_sources_summary)


