from datetime import date, datetime, timedelta
import json
import time
import re


class TokenRow:
    """
    Abstract class for storing nested set tree token data.

    Attributes
    ---------
        tokenId (int): stored token id
        token (str): stored token name
        lft (int): stored token left index
        rgt (int): stored token right index
        children (arr[TokenRow]): stored list of children of the parent token
        
    Raises
    ---------
        Exception: if smoother is instantiated directly
    """

    def __init__(self, tokenId, token, lft, rgt):
        self.tokenId = tokenId
        self.token = token
        self.lft = lft
        self.rgt = rgt
        self.children = []    
        
    def AddChild(self, child):
        """
        Function adds a child to the nested set tree as the last leaf
        """
        if type(child) != TokenRow:
            raise TypeError('Child Must Be TokeRow Type')
        self.children.append(child)

    def GetChildren(self):
        """
        Function returns the list of children for the parent token
        """
        return self.children
    
    def hasChildren(self):
        """
        Function returns true if parent has any children
        """
        return len(self.children) > 0
    
    def addChild(self, child):
        """
        Function adds a child to the parent node as the first child
        """
        self.children.insert(0, child)
    
    def __repr__(self):
        return "TokenRow(tokenId={}, token='{}', lft={}, rgt={}, attributeId='{}')". \
        format(self.tokenId, self.token, self.lft, self.rgt, self.attribute_id)