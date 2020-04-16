# LDAP Server Set-up for Dex Authentication

## Setting up a LDAP Database

1. Deploy a new LDAP Server as a StatefulSet.

    ```bash
    kubectl apply -f LDAP-server.yaml
    ```

2. Seed the LDAP database with new entries

    ```bash
    kubectl exec -it -n kubeflow ldap-0 -- bash
    ldapadd -x -D "cn=admin,dc=example,dc=com" -W
    # Enter password "admin".
    # Press Ctrl+D to complete after pasting the snippet below.
    ```

    <details>
    <summary>Copy and paste paragraph by paragraph</summary>

    ```ldif
    # If you used the OpenLDAP Server deployment in step 1,
    # then this object already exists.
    # If it doesn't, uncomment this.
    #dn: dc=example,dc=com
    #objectClass: dcObject
    #objectClass: organization
    #o: Example
    #dc: example
            
    dn: ou=People,dc=example,dc=com
    objectClass: organizationalUnit
    ou: People
            
    dn: cn=Nick Kiliadis,ou=People,dc=example,dc=com
    objectClass: person
    objectClass: inetOrgPerson
    givenName: Nick
    sn: Kiliadis
    cn: Nick Kiliadis
    uid: nkili
    mail: nkili@example.com
    userpassword: 12341234
            
    dn: cn=Robin Spanakopita,ou=People,dc=example,dc=com
    objectClass: person
    objectClass: inetOrgPerson
    givenName: Robin
    sn: Spanakopita
    cn: Robin Spanakopita
    uid: rspanakopita
    mail: rspanakopita@example.com
    userpassword: 43214321
            
    # Group definitions.
            
    dn: ou=Groups,dc=example,dc=com
    objectClass: organizationalUnit
    ou: Groups
            
    dn: cn=admins,ou=Groups,dc=example,dc=com
    objectClass: groupOfNames
    cn: admins
    member: cn=Nick Kiliadis,ou=People,dc=example,dc=com
            
    dn: cn=developers,ou=Groups,dc=example,dc=com
    objectClass: groupOfNames
    cn: developers
    member: cn=Nick Kiliadis,ou=People,dc=example,dc=com
    member: cn=Robin Spanakopita,ou=People,dc=example,dc=com
    ```

    </details>

## Using LDAP server with Dex

1. Get current Dex config from the corresponding Config Map

    ```bash
    kubectl get configmap dex -n auth -o jsonpath='{.data.config\.yaml}' > dex-config.yaml
    ```

2. Add the LDAP-specific options ([example](dex-config-ldap-partial.yaml))

3. Append the LDAP config section to the dex config

    ```bash
    cat dex-config.yaml dex-config-ldap-partial.yaml > dex-config-final.yaml
    ```
4. Apply the new config

    ```bash
    kubectl create configmap dex --from-file=config.yaml=dex-config-final.yaml -n auth --dry-run -oyaml | kubectl apply -f -
    ```
5. Restart the Dex deployment

    ```bash
    kubectl rollout restart deployment dex -n auth
    ```