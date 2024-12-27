import logging
from passlib.totp import TOTP
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


# Create TOTP instance
def create_totp_instance(secret=None, algorithm=None, digits=None, period=None):
    return TOTP(key=secret, alg=algorithm, digits=digits, period=period)


totp = create_totp_instance(Config.OTP_SECRET, Config.OTP_ALGORITHM, Config.OTP_LENGTH, Config.OTP_VALIDITY)


# Generate OTP
def generate_otp():
    otp = totp.generate()
    return {"token": otp.token, "expires_at": otp.expiry}


# Verify OTP
def verify_otp(otp):
    if isinstance(otp, int) and len(otp) == Config.OTP_LENGTH:
        try:
            return totp.verify(otp)
        except Exception as e:
            logging.error(f"Unexpected error during OTP verification: {e}")
            return False
    else:
        logging.error("Invalid OTP format")
        return False
