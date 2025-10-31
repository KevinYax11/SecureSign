import rsa

def generar_claves(ruta_publica, ruta_privada, bits=2048):
    """
    Generates a new RSA key pair and saves them to files.
    Returns True on success, False on error.
    """
    try:
        (public_key, private_key) = rsa.newkeys(bits)
        
        with open(ruta_publica, "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))
            
        with open(ruta_privada, "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))
            
        return True
    except Exception as e:
        print(f"Error generating keys: {e}")
        return False

def firmar_documento(ruta_documento, ruta_clave_privada, ruta_firma_salida):
    """
    Signs a document using a private key.
    Returns True on success, False on error.
    """
    try:
        with open(ruta_clave_privada, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
            
        with open(ruta_documento, "rb") as f:
            mensaje = f.read()
            
        firma = rsa.sign(mensaje, private_key, "SHA-256")
        
        with open(ruta_firma_salida, "wb") as f:
            f.write(firma)
            
        return True
    except Exception as e:
        print(f"Error signing document: {e}")
        return False

def verificar_firma(ruta_documento, ruta_firma, ruta_clave_publica):
    """
    Verifies a signature against a document and a public key.
    Returns True if valid, False if invalid or error.
    """
    try:
        with open(ruta_clave_publica, "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
            
        with open(ruta_documento, "rb") as f:
            mensaje = f.read()
            
        with open(ruta_firma, "rb") as f:
            firma = f.read()
            
        rsa.verify(mensaje, firma, public_key)
        
        return True
    
    except rsa.VerificationError:
        print("Verification failed: Signature does not match.")
        return False
    except Exception as e:
        print(f"Error during verification: {e}")
        return False