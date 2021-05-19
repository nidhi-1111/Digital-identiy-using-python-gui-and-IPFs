// "SPDX-License-Identifier: UNLICENSED"
pragma solidity ^0.7.4;

contract Digital {
    address payable contractOwner;
    mapping (address => mapping(uint16 => string)) mapOfHash;
    mapping (string => mapping(uint16 => address)) hashOwner;
    
    constructor() {
        contractOwner = msg.sender;
    }
    
    // modifiers
    
    modifier onlyContractOwner() {
        require(contractOwner == msg.sender);
        _;
    }
    
    modifier isHashOwner(string memory hashVal, uint16 hashNo) {
        require(hashOwner[hashVal][hashNo] == msg.sender);
        _;
    }
    
    // public function
    
    // hash number mean 1.for passport 2 for addharcard like that
    function addHash(string memory hashOfIpfs, uint16 hashNo) public {
        _addHash(hashOfIpfs, hashNo);
    }
    
    // check if currentHash hash owner is same and if same then update the value
    function updateHash(string memory hashOfIpfs, string memory currentHash, uint16 hashNo) public isHashOwner(currentHash, hashNo) {
        _updateHash(hashOfIpfs, hashNo);
    }
    
    // check if person is hashOwner if it is then he can delete the hash
    function deleteHash(string memory hashOfIpfs, uint16 hashNo) public isHashOwner(hashOfIpfs, hashNo) {
        _deleteHash(hashOfIpfs, hashNo);
    }
    
    // give the appropriate hash of document
    function displayHash(uint16 hashNo) public view returns(string memory) {
        // check if value is not empty
        require(keccak256(abi.encodePacked((mapOfHash[msg.sender][hashNo]))) != keccak256(abi.encodePacked((""))));
        return mapOfHash[msg.sender][hashNo];
    }
    
    
    // owner can destroy the contract
    function destroy() public onlyContractOwner{
        selfdestruct(contractOwner);
    }
    
    
    // private functions
    
    function _addHash(string memory hashOfIpfs, uint16 hashNo) private {
        mapOfHash[msg.sender][hashNo] = hashOfIpfs;
        hashOwner[hashOfIpfs][hashNo] = msg.sender;
    }
    
    function _updateHash(string memory hashOfIpfs, uint16 hashNo) private {
        mapOfHash[msg.sender][hashNo] = hashOfIpfs;
    }
    
    function _deleteHash(string memory hashOfIpfs, uint16 hashNo) private {
        delete mapOfHash[msg.sender][hashNo];
        delete hashOwner[hashOfIpfs][hashNo];
    }
}
