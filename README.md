# HadesFit

![HadesFit Logo](https://github.com/haybnzz/HadesFit/blob/main/HadesFit.png?raw=true)

[![Python - HadesFit](https://img.shields.io/static/v1?label=Python&message=HadesFit&style=for-the-badge&logo=python&logoSize=auto&labelColor=4B4453&color=FF6F61)](https://github.com/haybnzz/HadesFit)
[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&style=for-the-badge&logo=open-source-initiative&logoSize=auto&labelColor=4B4453&color=FFD166)](https://github.com/haybnzz/HadesFit/blob/main/LICENSE)
[![Python Version](https://img.shields.io/static/v1?label=Python&message=3.6%2B&style=for-the-badge&logo=python&logoSize=auto&labelColor=4B4453&color=06D6A0)](https://www.python.org/downloads/)
[![GitHub Issues](https://img.shields.io/github/issues/haybnzz/HadesFit?style=for-the-badge&logo=github&logoSize=auto&labelColor=4B4453&color=118AB2)](https://github.com/haybnzz/HadesFit/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/haybnzz/HadesFit?style=for-the-badge&logo=github&logoSize=auto&labelColor=4B4453&color=073B4C)](https://github.com/haybnzz/HadesFit/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/haybnzz/HadesFit?style=for-the-badge&logo=github&logoSize=auto&labelColor=4B4453&color=EF476F)](https://github.com/haybnzz/HadesFit/stargazers)
![Profile Views](https://komarev.com/ghpvc/?username=haybnzz&style=for-the-badge&logo=github&logoSize=auto&labelColor=4B4453&color=FFD166)





>HadesFit is a Python-based application designed to streamline the integration of fitness data from Google Fit and various smartwatches into a unified fitness tracking system. 

**Purpose:**  
The primary goal of HadesFit is to provide users with a seamless way to 🔄 aggregate, 📊 analyze, and 📈 visualize their fitness data from multiple sources. By connecting with Google Fit, HadesFit can pull in data like steps 🚶, heart rate ❤️, calories burned 🔥, and sleep patterns 🛌, allowing users to see all their health metrics in one place.

**Functionality:**

- **Google Fit Integration:**  
  HadesFit uses Google Fit APIs to fetch and sync data. This includes activity information such as step counts, workout sessions, and nutritional data if connected through compatible apps. Users can grant or revoke access to this data via Google Fit settings, ensuring 🔒 privacy and control.

- **Smartwatch Connectivity:**  
  Beyond Google Fit, HadesFit supports integration with smartwatches. Depending on the smartwatch model, this might require direct integration through Health Connect or third-party syncing solutions. Supported devices include those running Wear OS ⌚, as well as specific brands like Samsung, Garmin, and Polar, which have their own methods of syncing with Google Fit.


# HadesFit Installation & Setup

## Installation

### Prerequisites
- Python 3.6 or higher installed on your system.
- A Google account for Google Fit API access.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/haybnzz/HadesFit.git
   cd HadesFit
   pip install -r requirements.txt
   python app.py



## Configure Google Fit API:
To use the Google Fit API with HadesFit, you need to set up a project in the **Google Cloud Console**. Follow the steps below to get started.



### Google Cloud Console Setup

>#### **Create a Project**
>1. Navigate to [Google Cloud Console](https://console.cloud.google.com/).
>2. Click on the project dropdown at the top, then click **New Project**.
>3. Name your project (e.g., **HadesFit**) and click **Create**.

#### **Enable Google Fit API**

1. In your new project, go to **APIs & Services > Dashboard**.
2. Click **Enable APIs and Services**.
3. Search for `Fitness API`, select it, and click **Enable**.

#### **Create Credentials**
1. From the sidebar, select **Credentials**.
2. Click **Create Credentials > OAuth client ID**.
    - Choose **Application type**: Desktop app (or Other if you're not using a web server).
    - Name your client ID (e.g., **HadesFit Client**).
    - Click **Create**.
3. Download the JSON file named something like `client_secret_XXXXX.json`.
4. Reaname to `credentials.json`


### **Configure HadesFit**

#### **Place the JSON File**
Move the downloaded `credtilasjson` into your HadesFit project folder.

#### **Set Environment Variables**
Set the environment variable to point to your credentials file:





## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

**Unauthorized use is strictly prohibited.**

📧 Email: cubedimension@protonmail.com  



### Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haybnzz">](https://github.com/haybnzz)  

[<img src="https://avatars.githubusercontent.com/u/144106684?s=64&v=4" width="64" height="64" alt="Glitchesminds">](https://github.com/Glitchesminds)

## ☕ Support

If you find this project helpful, consider buying us a coffee with cookies:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%23FFDD00?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/codeglitch)

