---
title: "Building StarMade from source"
sidebar_label: "Build from source"
description: "Instructions for building the StarMade codebase from source (for internal developers)."
---

# Building StarMade from source

This page is intended for developers who have access to the StarMade source repository. If you are looking for general instructions on how to mod StarMade, see the [modding basics](../modding-basics.md) page.

Most players don't have access to the upstream StarMade source repository, so these instructions are only useful for internal development and contributors.

## Prerequisites

- Java
  - Release branch: Java 8 (development uses Java 8 but the release branch is built for Java 7 compatibility; set your IDE language level accordingly). Download: https://adoptium.net/temurin/releases/?os=any&arch=any&version=8
  - Universe Update branch: Java 23. Download: https://adoptium.net/temurin/releases/?os=any&arch=any&version=23
- Build tool
  - Release branch: Apache Ant — https://ant.apache.org/bindownload.cgi
  - Universe Update branch: Gradle — https://gradle.org/install/
- IDE
  - IntelliJ IDEA (Community or Ultimate) recommended: https://www.jetbrains.com/idea/download/

## Building the release branch

1. Clone the repository and check out the `release` branch:

   ```powershell
   # example (Windows PowerShell)
   git clone <repo-url>
   cd <repo-name>
   git checkout release
   ```

2. Copy the example environment file and populate required values (if present):

   ```powershell
   Copy-Item -Path scripts\.env_example -Destination .env
   # then edit .env to set required variables
   ```

3. Run the platform-specific build script from the `scripts` folder.

   - Windows (PowerShell):

     ```powershell
     scripts\build_windows.ps1
     ```

   - Linux (bash):

     ```bash
     scripts/build_linux.sh
     ```

   - macOS (bash):

     ```bash
     scripts/build_macos.sh
     ```

## Building the Universe Update branch

1. Clone the repository and check out the `master` branch (or the branch used for the Universe Update):

   ```bash
   git clone <repo-url>
   cd <repo-name>
   git checkout master
   ```

2. Build using Gradle from the repository root:

   ```bash
   gradle build
   ```


<!-- end of file -->
