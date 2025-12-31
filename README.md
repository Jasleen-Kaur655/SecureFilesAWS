# Secure File Management System
**A Full-Stack, AWS-powered, Secure File Upload & Management Web App**

## Overview
This project is a secure file management system that allows users to:
- Register and login securely
- Upload files to private AWS S3 storage
- Generate temporary links for file sharing
- Manage and view files with access control

Built with a modern full-stack architecture, AWS cloud services, and CI/CD deployment.

## Features
- User authentication & authorization
- File upload & download with pre-signed S3 URLs
- Secure storage using AWS S3 and IAM policies
- Metadata storage in DynamoDB/RDS
- Dockerized backend & frontend
- CI/CD integration using GitHub Actions
- Easy-to-use React frontend with FastAPI backend

## Architecture
- **Frontend:** React.js (Login, File Upload, File List)
- **Backend:** FastAPI (Auth, File management, Temporary links)
- **Database:** DynamoDB/RDS for storing file metadata
- **Cloud Storage:** AWS S3 with pre-signed URLs
- **Security:** IAM roles for secure access, no hardcoded keys
- **Deployment:** Docker containers with GitHub Actions CI/CD

## Technologies
- React.js
- FastAPI
- AWS S3 & IAM
- DynamoDB / RDS
- Docker
- GitHub Actions (CI/CD)
- Python & JavaScript

## Project Pipeline
## Project Pipeline
<img
  width="500"
  alt="Secure File Management System Pipeline"
  src="https://github.com/Jasleen-Kaur655/SecureFilesAWS/blob/main/Images/Flowchart.png?raw=true"
/>

## Screenshots

**Login Page**  
![Login Page](Images/Login_Page.png)

**File Uploaded Page**  
![File Uploaded Page](Images/File_uploaded_page.png)

**Deleted File Page**  
![Deleted File Page](Images/Deleted_file_page.png)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Jasleen-Kaur655/SecureFilesAWS.git

2. Backend dependencies:
   cd backend
   pip install -r requirements.txt

3. Frontend dependencies:
   cd frontend
   npm install

Set up AWS credentials and environment variables

Run backend and frontend

## Usage

Register/Login as a user
Upload files securely
View your file list
Delete files

Generate temporary download links






