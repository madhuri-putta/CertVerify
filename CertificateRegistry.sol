// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract CertificateRegistry {
    struct Certificate {
        string fileHash;
        string studentName;
        string course;
        string institute;
        uint256 timestamp;
        address issuer;
        bool isValid;
    }

    mapping(string => Certificate) public certificates;
    address public owner;

    event CertificateRegistered(string indexed fileHash, string studentName, string institute);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    function registerCertificate(
        string memory _fileHash,
        string memory _studentName,
        string memory _course,
        string memory _institute
    ) public {
        // In a real app, we might restrict this to authorized issuers
        // For now, allow anyone or restrict to owner based on requirements
        // require(msg.sender == owner, "Only owner can register");

        require(bytes(certificates[_fileHash].fileHash).length == 0, "Certificate already registered");
        
        certificates[_fileHash] = Certificate({
            fileHash: _fileHash,
            studentName: _studentName,
            course: _course,
            institute: _institute,
            timestamp: block.timestamp,
            issuer: msg.sender,
            isValid: true
        });

        emit CertificateRegistered(_fileHash, _studentName, _institute);
    }

    function verifyCertificate(string memory _fileHash) public view returns (
        bool isValid,
        string memory studentName,
        string memory course,
        string memory institute,
        uint256 timestamp,
        address issuer
    ) {
        Certificate memory cert = certificates[_fileHash];
        if (bytes(cert.fileHash).length == 0) {
            return (false, "", "", "", 0, address(0));
        }
        return (
            cert.isValid,
            cert.studentName,
            cert.course,
            cert.institute,
            cert.timestamp,
            cert.issuer
        );
    }
}
