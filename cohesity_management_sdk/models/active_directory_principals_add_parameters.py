# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.


class ActiveDirectoryPrincipalsAddParameters(object):

    """Implementation of the 'ActiveDirectoryPrincipalsAddParameters' model.

    Specifies the settings for adding new users and groups
    for Active Directory principals.
    These users and groups are added to the Cohesity Cluster.
    You cannot create users and groups in the default Cohesity domain
    called 'LOCAL' using this operation.

    Attributes:
        description (string): Specifies a description about the user or
            group.
        domain (string): Specifies the domain of the Active Directory where
            the referenced principal is stored.
        object_class (ObjectClassActiveDirectoryPrincipalsAddParametersEnum):
            Specifies the type of the referenced Active Directory principal.
            If 'kGroup', the referenced Active Directory principal is a group.
            If 'kUser', the referenced Active Directory principal is a user.
            'kUser' specifies a user object class. 'kGroup' specifies a group
            object class. 'kComputer' specifies a computer object class.
            'kWellKnownPrincipal' specifies a well known principal.
        principal_name (string): Specifies the name of the Active Directory
            principal, that will be referenced by the group or user. The name
            of the Active Directory principal is used for naming the new group
            or user on the Cohesity Cluster.
        restricted (bool): Whether the principal is a restricted principal. A
            restricted principal can only view the objects he has permissions
            to.
        roles (list of string): Array of Roles.  Specifies the Cohesity roles
            to associate with this user or group such as 'Admin', 'Ops' or
            'View'. The Cohesity roles determine privileges on the Cohesity
            Cluster for this group or user. For example if the 'joe' user is
            added for the Active Directory 'joe' user principal and is
            associated with the Cohesity 'View' role, 'joe' can log in to the
            Cohesity Dashboard and has a read-only view of the data on the
            Cohesity Cluster.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description":'description',
        "domain":'domain',
        "object_class":'objectClass',
        "principal_name":'principalName',
        "restricted":'restricted',
        "roles":'roles'
    }

    def __init__(self,
                 description=None,
                 domain=None,
                 object_class=None,
                 principal_name=None,
                 restricted=None,
                 roles=None):
        """Constructor for the ActiveDirectoryPrincipalsAddParameters class"""

        # Initialize members of the class
        self.description = description
        self.domain = domain
        self.object_class = object_class
        self.principal_name = principal_name
        self.restricted = restricted
        self.roles = roles


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
        description = dictionary.get('description')
        domain = dictionary.get('domain')
        object_class = dictionary.get('objectClass')
        principal_name = dictionary.get('principalName')
        restricted = dictionary.get('restricted')
        roles = dictionary.get('roles')

        # Return an object of this model
        return cls(description,
                   domain,
                   object_class,
                   principal_name,
                   restricted,
                   roles)


