# Copyright (c) 2021 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
from typing import Union
from bip_utils.ecc import IPublicKey, Ed25519PublicKey, Secp256k1PublicKey


class AddrUtils:
    """ Class container for address utility functions. """

    @staticmethod
    def ValidateAndGetEd25519Key(pub_key: Union[bytes, IPublicKey]) -> Ed25519PublicKey:
        """ Validate and get a ed25519 public key.

        Args:
            pub_key (bytes or IPublicKey object): Public key bytes or object

        Returns:
            Ed25519PublicKey object: Ed25519PublicKey object

        Raises:
            TypeError: If the public key is not ed25519
        """
        if isinstance(pub_key, bytes):
            pub_key = Ed25519PublicKey(pub_key)
        elif not isinstance(pub_key, Ed25519PublicKey):
            raise TypeError("A ed25519 public key is required")

        return pub_key

    @staticmethod
    def ValidateAndGetSecp256k1Key(pub_key: Union[bytes, IPublicKey]) -> Secp256k1PublicKey:
        """ Validate and get a secp256k1 public key.

        Args:
            pub_key (bytes or IPublicKey object): Public key bytes or object

        Returns:
            Secp256k1PublicKey object: Secp256k1PublicKey object

        Raises:
            TypeError: If the public key is not secp256k1
        """
        if isinstance(pub_key, bytes):
            pub_key = Secp256k1PublicKey(pub_key)
        elif not isinstance(pub_key, Secp256k1PublicKey):
            raise TypeError("A secp256k1 public key is required")

        return pub_key
