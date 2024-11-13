# Dockerized Nginx Servers with Automated Testing - Home Assignment

## Overview
- **Nginx Server Container**: Built from Ubuntu 22.04, configured with two servers:
  - **Port 8080**: Returns a custom HTML response.
  - **Port 8081**: Returns an HTTP 503 error.

- **Tester Container**: Runs a Python script to test the Nginx servers.

A GitHub Actions workflow automates building the images, running the tests, and publishes an artifact indicating success (`succeeded`) or failure (`fail`).

## Quick Start

1. **Build and run the containers**:

   ```bash
   docker compose up --build -d
   ```

2. **Check test results**:

   ```bash
   docker logs nginx_tester
   ```

3. **Shut down the environment**:

   ```bash
   docker compose down
   ```

## Screenshots

### 1. **Success Scenario**
<img width="1275" alt="Success scenario" src="https://github.com/user-attachments/assets/d3309f60-9292-40d2-a8d6-e2825485a9a8">

### 2. **Failure Scenarios**
- **Deliberate Failure - Server 1** (Expected 200, Returned 201):
<img width="1260" alt="201 fail" src="https://github.com/user-attachments/assets/62749761-ac33-402f-a69d-cff80d3c7250">

- **Deliberate Failure - Server 2** (Expected 503, Returned 504):
<img width="1256" alt="504" src="https://github.com/user-attachments/assets/878b8dd8-6d7e-48cb-9b9e-3efeaee37cd3">

## Design Choices

- **Image Optimization**:
  - **Nginx Container**:
    - Used `ubuntu:22.04` (Ubuntu LTS Minimal).
    - Minimized size by installing only necessary packages and cleaning up caches.
    - Although slightly affecting the image size, implemented **Supervisor** for a more robust process management.

  - **Tester Container**:
    - Chose `python:3.9-alpine` for a smaller footprint.
    - Since I'm more familiar with Python, I Opted for it over Go although there was a potential for a further decrease of the image size.

**The Image Size for each:**

<img width="971" alt="image" src="https://github.com/user-attachments/assets/0315417b-c6cf-48e5-833e-625b1aec8274">

## Additional Notes

- **AI Use - Learning Resources**:
  - Utilized **ChatGPT** to efficiently address unfamiliar areas and adopt best practices - for full conversation [click here.](https://chatgpt.com/share/6730fdb5-ece4-8011-9cf3-9c73975e2b1a)
  - Used cursor.ai editor


    
  
