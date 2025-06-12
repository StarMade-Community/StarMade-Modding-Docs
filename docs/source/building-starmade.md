# Introduction
This page is specifically for internal use by the team to build StarMade from source. If you are looking for the general 
instructions on how to mod StarMade, please refer to the [modding basics](modding-basics.md).

Most players don't have access to the actual StarMade source repository (as of this writing, June 12, 2025), so this 
page won't be useful to them.
# Prerequisites
- Java 8 (Release branch) or Java 23 (Universe Update branch)
  - You can get Java 8 from [AdoptOpenJDK8](https://adoptium.net/temurin/releases/?os=any&arch=any&version=8).
    Note that while we use Java 8 for release branch development, the release branch is built in Java 7 for compatibility 
    reasons, and you should set your IDE's Language Level to 7.
  - You can get Java 23 from [AdoptOpenJDK23](https://adoptium.net/temurin/releases/?os=any&arch=any&version=23).
- Apache Ant (Release branch) or Gradle (Universe Update branch)
  - You can get Apache Ant from [Apache Ant](https://ant.apache.org/bindownload.cgi).
  - You can get Gradle from [Gradle](https://gradle.org/install/).
- IntelliJ IDEA Community Edition or Intellij IDEA Ultimate Edition
  - You can get IntelliJ IDEA from [JetBrains](https://www.jetbrains.com/idea/download/).
    Technically, you can use any IDE that supports Java, but IntelliJ is the one we use and recommend.
# Building the Release Branch
1. Clone the repository and ensure you are on the `release` branch.
2. There will be `.env_example` file in the `scripts` folder. Copy it to `.env` and fill in the required values.
3. Run the relevant build script in the `scripts` folder for your operating system:
   - For Windows: `build_windows.ps1`
   - For Linux: `build_linux.sh`
   - For MacOS: `build_macos.sh`
# Building the Universe Update Branch
1. Clone the repository and ensure you are on the `master` branch.
2. Run `gradle build` in the root directory of the repository.