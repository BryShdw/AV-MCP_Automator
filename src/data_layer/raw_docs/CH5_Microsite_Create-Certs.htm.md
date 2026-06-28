

# Create Certificates for Safari on iOS and iPadOS Platforms

Prior to running an HTML5 Web XPanel project on the Safari® browser for an iOS® or iPadOS® device, a secure communications certificate must be created that allows the project to communicate with a Crestron control system. The following procedures describe how to create and load this certificate.

## Prerequisites

The following procedures require access to the Windows® software command prompt, the Text Console tool in Crestron Toolbox™ software, and an iOS or iPadOS device with pin code access.

The following must be downloaded to your workstation (latest versions recommended):

- Crestron software tools
  - [Crestron Toolbox software](https://www.crestron.com/Support/Search-Results?c=4&m=undefined&q=crestron%20toolbox)
  - [Crestron database](https://www.crestron.com/support/search-results?c=4&m=10&q=crestron%20database)
  - [Device database](https://www.crestron.com/support/search-results?c=4&m=10&q=device%20database)
- OpenSSL
  - [OpenSSL binaries](https://wiki.openssl.org/index.php/Binaries)
  - [Win32/Win64 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) (the light 64-bit version is recommended)

## Create the Certificate Files

Use the following procedures to create a certificate for secure communications between the control system and the HTML5 Web XPanel project on Safari.

### Start the OpenSSL Command Prompt

A **start.bat** file will be present in the location where OpenSSL was installed on your workstation (such as **c:\\Program Files\\OpenSSL-Win64**). Opening this file will display a command prompt that will return the following information once it has loaded.

Copy

```
OpenSSL 1.1.1i  8 Dec 2020
built on: Tue Dec  8 20:54:45 2020 UTC
platform: VC-WIN64A
options:  bn(64,64) rc4(16x,int) des(long) idea(int) blowfish(ptr)
compiler: cl /Z7 /Fdossl_static.pdb /Gs0 /GF /Gy /MD /W3 /wd4090 /nologo /O2
-DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_CPUID_OBJ -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT
-DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM
-DKECCAK1600_ASM -DRC4_ASM -DMD5_ASM -DAESNI_ASM -DVPAES_ASM -DGHASH_ASM -DECP_NISTZ256_ASM
-DX25519_ASM -DPOLY1305_ASM -D_USING_V110_SDK71_ -D_WINSOCK_DEPRECATED_NO_WARNINGS
-D_WIN32_WINNT=0x0502
OPENSSLDIR: "C:\Program Files\Common Files\SSL"
ENGINESDIR: "C:\Program Files\OpenSSL\lib\engines-1_1"
Seeding source: os-specific
```

### Determine Subject Alternate Name Parameters

The subject alternate name parameters are used when creating the Certificate Signature Request (CSR) on the control system. To determine these parameters:

01. Open Crestron Toolbox software.
02. Open the Text Console tool and establish communications with the control system.
03. Issue the hostname and domain commands. Sample responses are provided below

Copy

```
CP3>hostname
Host Name: RS-CP3

CP3>domain
Device 0 Domain Name: router.home
```

07. Confirm that the concatenation of the host name and domain name (hostname.domain) is valid.
08. Issue the ping hostname.domain command into the OpenSSL console and record the provided IP address. Refer to the following example.

Copy

```
C:\users\yourName\Documents\caSignedCertsWorkarea>ping RS-CP3.router.home

Pinging RS-CP3.fios-router.home [192.168.1.244] with 32 bytes of data:
Reply from 192.168.1.255: bytes=32 time<1ms TTL=128
Reply from 192.168.1.255: bytes=32 time<1ms TTL=128
Reply from 192.168.1.255: bytes=32 time=1ms TTL=128
Reply from 192.168.1.255: bytes=32 time=1ms TTL=128

Ping statistics for 192.168.1.255:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms
```

In the example above, the fully qualified host name is **RS-CP3.router.home** and the IP address is **192.168.1.255**. These values would be used for the subject alternate name parameters when creating the CSR.

### Create the Certificate Signature Request (CSR)

Use the Text Console tool in Crestron Toolbox to issue the createscr console command to the control system. This command is used to generate a CSR for the control system as specified by the given parameters.

NOTE: Crestron Toolbox does not provide the ability to add the subject alternate names directly. Use the -s parameter for the createcsr command to allow the DNS and IP parameters as subject alternate names. For more information, refer to [Determine Subject Alternate Name Parameters](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Platforms/Create-Certs.htm#Determine_Subject_Alternate_Name_Parameters).

createcsr c:st:l:o:ou:cn:e \[-i:<option>\] \[-s:<altname>\[,<altname>\],...\]

- c \- Two-letter country code
- st \- State or province name
- l \- Locality or city name
- o \- Organization or company name
- ou \- Organizational unit name or division
- cn \- Site name or domain name
- e \- Email address
- -i \- Ignores blank parameters. <option> is true or false.
- -s \- Subject Alternative Name parameter(s); <altname\> is a type:value; valid types are DNS, IP, email, URI.

NOTE: Values that contain spaces must be enclosed in quotation marks.

**Example:** createcsr US:New Jersey:Rockleigh:Crestron:Dev:Fortune500Company:myuser@fortune500company.com -S:DNS:RS-CP3.router.home,IP:192.168.1.255

The CSR file ( **request.csr**) is created under within the **\\sys\** directory on the control system.

### Create a Certificate Workstation

Use the Windows command prompt to create and change directories to the following workstation on your computer for signed certificates.

Copy

```
mkdir c:\users\yourName\Documents\caSignedCertsWorkarea
cd c:\users\yourName\Documents\caSignedCertsWorkarea
```

#### Move the CSR File to the Workstation

Use the File Manager tool in Crestron Toolbox to move the **request.csr** file into the directory created in [Create a Certificate Workstation](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Platforms/Create-Certs.htm#Create_a_Certificate_Workstation).

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/CSR-1.png)

#### Review the CSR File

OpenSSL can be used to review the CSR file. In the following example, "X509v3 Subject Alternative Name" has been set in the CSR by the control system.

Copy

```
C:\users\yourName\Documents\caSignedCertsWorkarea>openssl req -text -noout -verify -in request.csr
verify OK
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: C = US, ST = New Jersey, L = Rockleigh, O = Crestron, OU = Dev,
        CN = Fortune500Company, emailAddress = myuser@fortune500company.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:e5:b5:f6:15:74:53:24:0c:cb:67:b9:29:c3:5c:
                    af:03:54:d9:c5:f4:76:38:72:20:f2:59:01:c2:38:
                    72:5f:a2:d3:ee:fa:0f:51:fc:c2:50:d2:06:e1:c2:
                    3b:87:00:1c:ed:00:c9:6e:3b:e2:5b:a7:a9:95:17:
                    bc:5a:2d:7f:e0:57:d8:a3:8e:69:cf:3a:5c:eb:f0:
                    e6:61:0f:90:e9:14:6f:75:0a:98:fe:9c:0c:c9:df:
                    79:91:e1:fc:a7:65:fa:42:11:5c:63:15:56:0b:66:
                    71:51:29:b6:e3:13:cd:a3:e5:f8:20:59:d2:ab:6f:
                    b5:00:8c:e4:4a:f0:a7:d4:71:8c:c3:ba:96:84:41:
                    c8:58:92:96:20:bc:39:d3:f1:fa:20:b2:02:ab:71:
                    46:57:29:51:9a:e6:07:9e:c4:8b:66:8f:46:de:18:
                    f8:05:97:49:e3:b8:39:11:bd:a8:21:75:cf:00:f1:
                    30:4d:32:97:d0:5c:f3:67:72:85:3d:ad:26:51:37:
                    d9:2d:22:6c:b0:2e:31:9d:67:6a:db:3b:bc:07:b3:
                    c3:95:3d:e6:3b:2c:78:f1:7e:f2:26:ac:e5:7f:81:
                    4e:90:7e:19:92:b6:ed:4f:ad:bf:60:99:57:0b:9e:
                    ca:f0:11:b5:3b:3e:11:25:8d:bd:f9:5d:73:c9:08:
                    f2:e7
                Exponent: 65537 (0x10001)
        Attributes:
        Requested Extensions:
            X509v3 Subject Alternative Name:
                DNS:RS-CP3.router.home, IP Address:192.168.1.244
    Signature Algorithm: sha256WithRSAEncryption
         7e:ba:82:3b:ec:27:53:64:c7:95:5b:25:04:6e:7a:f9:fd:f8:
         61:37:c8:91:5a:55:9c:4d:a3:37:c8:0e:f5:c3:6b:60:3c:db:
         a7:1f:a2:5d:9b:06:80:9f:15:db:a3:65:dc:6b:1d:34:95:d6:
         bd:bd:96:74:11:1e:bc:ff:81:c8:6e:64:69:2a:c9:be:a0:51:
         bf:1c:07:41:21:f4:e3:b1:06:fe:2e:b1:61:6b:46:09:17:9e:
         cb:da:72:44:8f:eb:5b:65:8f:5e:e4:99:e3:99:e8:1b:1d:a2:
         59:7c:05:67:64:d9:36:c0:e1:09:25:f1:2a:1f:bf:91:46:6d:
         35:dc:72:5a:ec:c3:a7:a3:d8:8b:e8:fa:2a:f8:eb:12:35:35:
         e8:7a:55:9b:99:67:31:f1:e9:24:0a:1b:5e:19:9c:0b:39:3b:
         dd:2d:86:45:e9:d8:48:7a:86:70:85:68:ad:36:24:db:4a:0a:
         00:a4:f7:36:c6:48:66:d1:cf:ca:da:5e:2a:98:3e:b3:48:f5:
         a7:f8:ab:0b:61:0f:97:34:de:47:77:0a:c5:a8:02:a0:b0:a5:
         48:9b:fc:c4:4f:63:5e:4a:e2:a4:77:3f:6a:bf:5b:a4:f1:c9:
         35:ca:ef:85:66:80:f6:e5:38:ba:6e:aa:4b:a0:b2:7b:87:85:
         9f:25:33:e7
```

#### Create a demoCA Environment

OpenSSL provides a mechanism to create root certificates and sign other certificates using the root certificate. A demoCA environment must be created using the Windows command prompt to facilitate this mechanism. Issue the following commands to create the required directories and files:

Copy

```
mkdir demoCA
mkdir demoCA\private
mkdir demoCA\newcerts
type nul > demoCA\index.txt
echo 01 > demoCA\serial
```

The created demoCA directory structure is as follows:

- **demoCA**: The root directory expected by OpenSSL
- **demoCA\\private**: The directory where the signing private key will be located
- **demoCA\\newCerts**: The directory where OpenSSL will output signed certificates
- **demoCA\\index.txt**: A database used by OpenSSL
- **demoCA\\serial**: A serial number used by OpenSSL

### Create the Private Signing Key

Issue the following command to create the private signing key file ( **cakey.pem**). The provided name and directory must be used verbatim.

Copy

```
openssl genrsa -out demoCA\private\cakey.pem 2048
```

### Create the Public Root Certificate

Issue the following command to create the public root certificate file ( **cacert.pem**). The provided name and directory must be used verbatim.

Copy

```
openssl req  -x509 -sha256 -new -key demoCA\private\cakey.pem -out demoCA\cacert.pem -days 730
-subj /CN="My Custom CA"
```

### Review the Certificate Files

At this point in the procedure, ensure that your certificate workstation includes the following files and directories

Copy

```
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA
C:\users\yourName\Documents\caSignedCertsWorkarea\request.csr
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\cacert.pem
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\index.txt
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\newcerts
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\private
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\serial
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\private\cakey.pem
```

Additionally, review the contents of your public root certificate. Ensure that X509v3 Basic Constraints is "critical" and that CA is "TRUE." The text output for a sample public root certificate is provided below.

Copy

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            13:ba:f6:52:57:92:22:fc:af:c6:61:11:81:6f:4a:7b:91:49:2c:bb
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = My Custom CA
        Validity
            Not Before: Jun 30 19:12:18 2021 GMT
            Not After : Jun 30 19:12:18 2023 GMT
        Subject: CN = My Custom CA
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:d9:61:43:b2:d8:f0:7f:f3:ea:b5:96:54:5a:eb:
                    0f:a8:cd:41:6a:18:d9:d7:64:26:a8:48:af:c5:c9:
                    a4:c6:90:c2:54:2b:e6:aa:52:c3:bb:de:d4:25:f4:
                    1a:bc:90:ea:4f:9c:bb:38:c3:cd:d8:03:0b:ac:68:
                    c6:df:5a:e3:4b:71:bc:e3:ea:7e:fb:da:0e:31:57:
                    51:5c:4f:52:f2:62:73:b4:e2:ab:66:c2:bb:c2:e2:
                    c6:f5:a3:0a:11:48:b1:e1:d2:64:29:d7:89:25:c0:
                    da:f7:f5:47:b9:fd:bd:11:ba:a8:5f:e2:e2:dd:bb:
                    ec:ff:88:ce:06:ac:f5:fa:78:56:a4:85:a0:a8:87:
                    18:84:9b:19:f3:a6:bb:89:e6:4f:1b:37:86:c7:1f:
                    27:73:95:19:fc:a9:6e:89:e0:d3:32:17:87:ed:2c:
                    92:b9:c2:0f:8b:5b:0e:05:4f:95:e1:15:12:3e:01:
                    9d:61:15:c1:10:c8:b9:36:bc:cf:47:0c:c9:98:08:
                    d4:9a:7c:44:5c:e9:ba:a9:9b:7a:9e:14:57:40:93:
                    22:47:b2:8b:39:a3:0a:4e:f0:40:1e:8e:8b:15:50:
                    92:72:76:6a:2e:4d:ab:26:a1:2b:af:a0:e2:40:bb:
                    d1:99:cf:5a:1d:67:b4:4c:b9:d9:c0:26:cd:6f:4b:
                    cc:7b
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier:
                AB:A1:5C:95:76:51:F0:2F:78:90:93:DB:51:6C:B0:86:5A:65:E5:C8
            X509v3 Authority Key Identifier:
                keyid:AB:A1:5C:95:76:51:F0:2F:78:90:93:DB:51:6C:B0:86:5A:65:E5:C8

            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
         18:2b:e4:b4:a0:f6:1d:d8:e0:66:a4:28:2b:db:2b:ed:ae:88:
         6f:d0:06:11:0e:03:36:b8:aa:3e:ce:26:cb:d8:27:2a:74:5e:
         e2:8e:04:65:6e:b5:ae:dc:07:84:39:ba:bb:c9:b8:d2:8b:28:
         d2:9f:52:ae:68:5c:90:57:3c:a0:d7:39:15:e1:b0:b4:35:a9:
         61:51:ea:d0:1a:d5:c9:9e:fd:b3:ea:9c:b0:e5:48:0b:56:16:
         b9:99:1e:f5:35:22:b4:f9:a8:95:07:af:81:b0:af:bc:84:90:
         73:a5:d6:24:f6:e8:8f:75:da:63:ce:a1:5e:49:7c:21:fe:91:
         c6:83:71:84:d0:50:b3:b8:12:5a:b2:ea:1e:a9:4d:8b:aa:ff:
         ea:df:3b:b3:2b:37:82:67:63:aa:28:2d:fe:a1:61:97:3d:f8:
         f2:a7:54:c9:4f:4e:ae:ca:fc:42:ad:bc:35:12:0c:49:eb:fa:
         f7:3d:55:49:42:15:35:43:08:6a:57:1e:41:8c:34:b4:b3:79:
         03:cf:98:52:04:ef:35:fe:20:4e:08:b8:91:9f:c3:1c:41:ef:
         cd:59:20:9c:b0:50:4b:a1:83:1b:98:f6:23:4d:7e:74:86:a8:
         37:30:5c:6e:c5:68:fc:8e:57:1a:6d:5c:a7:28:00:9c:e0:d2:
         b1:7c:92:d0
-----BEGIN CERTIFICATE-----
MIIDDzCCAfegAwIBAgIUE7r2UleSIvyvxmERgW9Ke5FJLLswDQYJKoZIhvcNAQEL
BQAwFzEVMBMGA1UEAwwMTXkgQ3VzdG9tIENBMB4XDTIxMDYzMDE5MTIxOFoXDTIz
MDYzMDE5MTIxOFowFzEVMBMGA1UEAwwMTXkgQ3VzdG9tIENBMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2WFDstjwf/PqtZZUWusPqM1BahjZ12QmqEiv
xcmkxpDCVCvmqlLDu97UJfQavJDqT5y7OMPN2AMLrGjG31rjS3G84+p++9oOMVdR
XE9S8mJztOKrZsK7wuLG9aMKEUix4dJkKdeJJcDa9/VHuf29EbqoX+Li3bvs/4jO
Bqz1+nhWpIWgqIcYhJsZ86a7ieZPGzeGxx8nc5UZ/KluieDTMheH7SySucIPi1sO
BU+V4RUSPgGdYRXBEMi5NrzPRwzJmAjUmnxEXOm6qZt6nhRXQJMiR7KLOaMKTvBA
Ho6LFVCScnZqLk2rJqErr6DiQLvRmc9aHWe0TLnZwCbNb0vMewIDAQABo1MwUTAd
BgNVHQ4EFgQUq6FclXZR8C94kJPbUWywhlpl5cgwHwYDVR0jBBgwFoAUq6FclXZR
8C94kJPbUWywhlpl5cgwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AQEAGCvktKD2HdjgZqQoK9sr7a6Ib9AGEQ4DNriqPs4my9gnKnRe4o4EZW61rtwH
hDm6u8m40oso0p9SrmhckFc8oNc5FeGwtDWpYVHq0BrVyZ79s+qcsOVIC1YWuZke
9TUitPmolQevgbCvvISQc6XWJPboj3XaY86hXkl8If6RxoNxhNBQs7gSWrLqHqlN
i6r/6t87sys3gmdjqigt/qFhlz348qdUyU9Orsr8Qq28NRIMSev69z1VSUIVNUMI
alceQYw0tLN5A8+YUgTvNf4gTgi4kZ/DHEHvzVkgnLBQS6GDG5j2I01+dIaoNzBc
bsVo/I5XGm1cpygAnODSsXyS0A==
-----END CERTIFICATE-----
```

### Modify the Default OpenSSL Configuration

Prior to creating the signed certificate using OpenSSL, the default configuration must be modified to support this.

To modify the default configuration:

1. Copy the configuration files to your certificate workstation using the following commands.

Copy

```
copy "C:\Program Files\Common Files\SSL\openssl.cnf" .\openssl.default.cnf
copy openssl.default.cnf openssl.config-for-certsigning.cnf
```

5. Open the **config-for-certsigning.cnf** file in a text editing application.
6. Remove the comment (#) next to copy\_extensions = copy to make the line active.

### Create a Configuration File to Describe Certificate Extensions

Create a new file named **openssl.extfile-for-certsigning.cnf** in your certificate workstation. The file must contain the following directives.

Copy

```
basicConstraints=critical,CA:FALSE
keyUsage = digitalSignature, keyEncipherment, keyAgreement
extendedKeyUsage = serverAuth
```

### Generate a New Certificate

After completing the instructions in the prior sections, issue the following command to generate a new certificate.

Copy

```
openssl ca -policy policy_anything -in request.csr
-config openssl.config-for-certsigning.cnf
-extfile openssl.extfile-for-certsigning.cnf
-out mynewcert.pem
```

After the request in validated, a certificate will be built like the one shown in the following example.

Copy

```
Certificate Details:
        Serial Number: 1 (0x1)
        Validity
            Not Before: Jun 30 19:25:04 2021 GMT
            Not After : Jun 30 19:25:04 2022 GMT
        Subject:
            countryName               = US
            stateOrProvinceName       = New Jersey
            localityName              = Rockleigh
            organizationName          = Crestron
            organizationalUnitName    = Dev
            commonName                = Fortune500Company
            emailAddress              = user@fortune500company.com
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Key Usage:
                Digital Signature, Key Encipherment, Key Agreement
            X509v3 Extended Key Usage:
                TLS Web Server Authentication
            X509v3 Subject Alternative Name:
                DNS:RS-CP3.router.home, IP Address:192.168.1.255
Certificate is to be certified until Jun 30 19:25:04 2022 GMT (365 days)
```

When prompted to sign and commit the certificate, enter y.

### Review the Updated Certificate Files

At this point in the procedure, ensure that your certificate workstation includes the following files and directories

Copy

```
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA
C:\users\yourName\Documents\caSignedCertsWorkarea\mynewcert.pem
C:\users\yourName\Documents\caSignedCertsWorkarea\openssl.config-for-certsigning.cnf
C:\users\yourName\Documents\caSignedCertsWorkarea\openssl.default.cnf
C:\users\yourName\Documents\caSignedCertsWorkarea\openssl.extfile-for-certsigning.cnf
C:\users\yourName\Documents\caSignedCertsWorkarea\request.csr
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\cacert.pem
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\index.txt
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\index.txt.attr
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\index.txt.old
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\newcerts
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\private
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\serial
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\serial.old
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\newcerts\01.pem
C:\users\yourName\Documents\caSignedCertsWorkarea\demoCA\private\cakey.pem
```

Additionally, review the contents of your signed certificate using OpenSSL to ensure the following x509v3 extensions are correct.

- **x509v3 Basic Constraints**: critical
- **CA**: False
- **x509v3 Key Usage**: Digital Signature, Key Encipherment, Key Agreement
- **x509v3 Extended Key Usage**: TLS Web Server Authentication
- **x509v3 Subject Alternate Name**: DNS:\[hostname.domain\], IP Address: \[ipaddress\]

The text output for a sample signed certificate is provided below.

Copy

```
ertificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 1 (0x1)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: CN = My Custom CA
        Validity
            Not Before: Jun 30 20:20:51 2021 GMT
            Not After : Jun 30 20:20:51 2022 GMT
        Subject: C = US, ST = New Jersey, L = Rockleigh, O = Crestron, OU = Dev,
        CN = Fortune500Company, emailAddress = myuser@fortune500company.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:e5:b5:f6:15:74:53:24:0c:cb:67:b9:29:c3:5c:
                    af:03:54:d9:c5:f4:76:38:72:20:f2:59:01:c2:38:
                    72:5f:a2:d3:ee:fa:0f:51:fc:c2:50:d2:06:e1:c2:
                    3b:87:00:1c:ed:00:c9:6e:3b:e2:5b:a7:a9:95:17:
                    bc:5a:2d:7f:e0:57:d8:a3:8e:69:cf:3a:5c:eb:f0:
                    e6:61:0f:90:e9:14:6f:75:0a:98:fe:9c:0c:c9:df:
                    79:91:e1:fc:a7:65:fa:42:11:5c:63:15:56:0b:66:
                    71:51:29:b6:e3:13:cd:a3:e5:f8:20:59:d2:ab:6f:
                    b5:00:8c:e4:4a:f0:a7:d4:71:8c:c3:ba:96:84:41:
                    c8:58:92:96:20:bc:39:d3:f1:fa:20:b2:02:ab:71:
                    46:57:29:51:9a:e6:07:9e:c4:8b:66:8f:46:de:18:
                    f8:05:97:49:e3:b8:39:11:bd:a8:21:75:cf:00:f1:
                    30:4d:32:97:d0:5c:f3:67:72:85:3d:ad:26:51:37:
                    d9:2d:22:6c:b0:2e:31:9d:67:6a:db:3b:bc:07:b3:
                    c3:95:3d:e6:3b:2c:78:f1:7e:f2:26:ac:e5:7f:81:
                    4e:90:7e:19:92:b6:ed:4f:ad:bf:60:99:57:0b:9e:
                    ca:f0:11:b5:3b:3e:11:25:8d:bd:f9:5d:73:c9:08:
                    f2:e7
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Key Usage:
                Digital Signature, Key Encipherment, Key Agreement
            X509v3 Extended Key Usage:
                TLS Web Server Authentication
            X509v3 Subject Alternative Name:
                DNS:RS-CP3.router.home, IP Address:192.168.1.255
    Signature Algorithm: sha256WithRSAEncryption
         16:7c:af:a9:69:ef:0b:d7:bb:c6:13:07:89:2a:c7:75:95:19:
         43:f5:93:1f:ac:83:6f:75:38:9f:cb:51:13:b1:03:c2:44:6d:
         a4:f5:57:e3:75:3a:02:2e:9a:e8:94:e0:72:e4:ef:32:76:e3:
         14:1b:59:fd:fe:f2:08:26:16:bb:92:89:d8:9c:a5:0e:29:d9:
         67:e6:5f:c2:34:62:e4:f6:4e:74:17:45:e6:25:64:df:36:46:
         0f:cc:35:95:c9:de:2a:41:8a:61:f1:09:5a:47:6e:bc:67:23:
         00:07:5c:b2:17:82:20:14:d7:80:00:a1:f6:9a:27:ee:ef:af:
         6c:55:29:70:62:42:e5:19:73:2e:f0:60:30:b8:5a:a3:43:da:
         67:d3:e4:47:98:67:ad:92:e4:ae:30:48:63:49:a9:ac:51:af:
         d8:eb:67:51:dc:87:25:15:84:75:f1:fd:77:ac:bc:d9:59:f9:
         c3:9d:6e:00:1f:4e:df:2e:a1:a7:fb:8d:cc:12:f6:16:d9:8a:
         55:6d:7f:9f:e2:fb:1c:e1:3b:98:49:72:67:f4:fa:33:97:86:
         91:bf:2a:52:9c:60:b1:f0:85:40:49:4a:be:70:7f:9d:ee:b4:
         bb:33:53:1e:36:76:cf:00:16:ff:69:b4:2f:a8:e7:fe:4c:ea:
         08:0a:e1:82
-----BEGIN CERTIFICATE-----
MIIDjzCCAnegAwIBAgIBATANBgkqhkiG9w0BAQsFADAXMRUwEwYDVQQDDAxNeSBD
dXN0b20gQ0EwHhcNMjEwNjMwMjAyMDUxWhcNMjIwNjMwMjAyMDUxWjCBoDELMAkG
A1UEBhMCVVMxEzARBgNVBAgMCk5ldyBKZXJzZXkxEjAQBgNVBAcMCVJvY2tsZWln
aDERMA8GA1UECgwIQ3Jlc3Ryb24xDDAKBgNVBAsMA0RldjEaMBgGA1UEAwwRRm9y
dHVuZTUwMENvbXBhbnkxKzApBgkqhkiG9w0BCQEWHG15dXNlckBmb3J0dW5lNTAw
Y29tcGFueS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDltfYV
dFMkDMtnuSnDXK8DVNnF9HY4ciDyWQHCOHJfotPu+g9R/MJQ0gbhwjuHABztAMlu
O+Jbp6mVF7xaLX/gV9ijjmnPOlzr8OZhD5DpFG91Cpj+nAzJ33mR4fynZfpCEVxj
FVYLZnFRKbbjE82j5fggWdKrb7UAjORK8KfUcYzDupaEQchYkpYgvDnT8fogsgKr
cUZXKVGa5geexItmj0beGPgFl0njuDkRvaghdc8A8TBNMpfQXPNncoU9rSZRN9kt
ImywLjGdZ2rbO7wHs8OVPeY7LHjxfvImrOV/gU6QfhmStu1Prb9gmVcLnsrwEbU7
PhEljb35XXPJCPLnAgMBAAGjXDBaMAwGA1UdEwEB/wQCMAAwCwYDVR0PBAQDAgOo
MBMGA1UdJQQMMAoGCCsGAQUFBwMBMCgGA1UdEQQhMB+CF1JTLUNQMy5maW9zLXJv
dXRlci5ob21lhwTAqAH0MA0GCSqGSIb3DQEBCwUAA4IBAQAWfK+pae8L17vGEweJ
Ksd1lRlD9ZMfrINvdTify1ETsQPCRG2k9VfjdToCLprolOBy5O8yduMUG1n9/vII
Jha7konYnKUOKdln5l/CNGLk9k50F0XmJWTfNkYPzDWVyd4qQYph8QlaR268ZyMA
B1yyF4IgFNeAAKH2mifu769sVSlwYkLlGXMu8GAwuFqjQ9pn0+RHmGetkuSuMEhj
SamsUa/Y62dR3IclFYR18f13rLzZWfnDnW4AH07fLqGn+43MEvYW2YpVbX+f4vsc
4TuYSXJn9Pozl4aRvypSnGCx8IVASUq+cH+d7rS7M1MeNnbPABb/abQvqOf+TOoI
CuGC
-----END CERTIFICATE-----
```

## Load the Certificate Files

The following procedures describe how to load various certificate files to the control system and the iOS or iPadOS device.

### Copy the Certificate Output Files

Issue the following commands to copy the required certificate output files to your certificate workstation.

Copy

```
copy mynewcert.pem mynewcert.cer
copy demoCA\cacert.pem mycacert.cer
```

### Load Certificate Files to the Control System

The root and signed certificate files must be loaded to the control system as follows:

01. Open Crestron Toolbox software.
02. Establish a connection to the control system.
03. Open the **SSL Management** function.
04. Select **Upload Root Certificate** from the **Certificate Management** drop-down menu.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Root-Cert.png)

06. Navigate to and select the outputted root certificate file in your certificate workstation ( **mycacert.cer**).
07. Select **Upload Signed Certificate** from the **Certificate Management** drop-down menu.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Signed-Cert.png)

09. Navigate to and select the outputted signed certificate file in your certificate workstation ( **mynewcert.cer**).
10. Fill the **CA-Signed** radio button to have the device use CA-signed certificates.

### Load the Root Certificate to the iOS or iPadOS Device

The root certificate file must be loaded to the iOS or iPadOS device as follows:

01. Create a new email message and attach the root certificate file ( **mycacert.cer**).
02. Send the email to an address that can be received by the target iOS or iPadOS device.
03. Open the received email in the iOS or iPadOS device and tap the root certificate file. The certificate will be downloaded to the device as a new profile.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-1.png)

05. Open the **Settings** app.
06. Navigate to **General** > **Profiles & Device Management**.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-2.png)

08. Tap the new root certificate profile.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-3.png)

10. Click **Install** in the top-right corner of the screen. A dialog box is displayed confirming the installation.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-4.png)

12. Tap **Install** in the dialog box to complete the installation.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-6.png)

14. Navigate to **General** > **Certificate Trust Settings**.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-7.png)

16. Turn on the toggle next to the root certificate. A dialog box is displayed with a warning message.
17. Tap **Continue** in the dialog box to trust the root certificate.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/iOS-8.png)

## Test the Connection

Once all certificate files have been created and loaded to the appropriate devices, launch the HTML5 Web XPanel project from the Safari web browser on your iOS or iPadOS device by entering the fully qualified host name or IP address into the web browser.

The HTML5 Web XPanel project should load successfully with a status of **Connected**.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/XPanel.png)