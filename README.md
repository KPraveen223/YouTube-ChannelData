# YouTube Channel Data Retrieval Web Application

## Overview
This project is a web application that allows users to retrieve comprehensive video data from a specified YouTube channel. By simply entering the channel name, users can generate and download an Excel file containing details such as video titles, descriptions, views, likes, comments, and more. The application utilizes the YouTube Data API to gather channel statistics and video details, and it is built using Flask, Python, and Pandas for data handling and export.

## Features
- **User-Friendly Interface:** A clean and intuitive HTML form where users can input the name of a YouTube channel.
- **YouTube Data Retrieval:** Uses the YouTube Data API to fetch channel statistics and video details such as:
  - Video Title
  - Description
  - Published Date
  - Views, Likes, Comments
  - Video Duration
  - Video URL
  - Any relevant course URLs found in the description
- **Data Export:** The retrieved data is compiled into an Excel file that the user can download.
- **Responsive Design:** The application is designed to be mobile-friendly and accessible on different devices.

## How It Works
1. **User Input:** Users enter the name of a YouTube channel in the input form.
2. **Channel Verification:** The application checks if the channel exists in a pre-defined dictionary of channel names and corresponding IDs.
3. **Data Retrieval:** Upon finding the channel, the app:
   - Retrieves channel statistics such as the number of subscribers, views, and total videos.
   - Extracts video IDs from the channel's playlist.
   - Fetches detailed information on each video, including video stats and any relevant course URLs mentioned in the video description.
4. **Excel File Generation:** All video data is compiled into an Excel file and made available for download.
   
## Technologies Used
- **Python**: The backend logic of the application is powered by Python.
- **Flask**: Flask is used to handle routing and manage the web interface.
- **YouTube Data API**: Used to fetch channel and video data.
- **Pandas**: Employed to process and organize video data, and generate an Excel file for export.
- **HTML/CSS**: Provides the front-end interface, styled with CSS for a clean and responsive design.
- **Google API Client Library**: To interact with YouTube’s API.

## Setup and Installation

### Prerequisites
- Python 3.10 or later
- Google Cloud API Key with YouTube Data API v3 enabled

**Usage**:
   - Open the application in your web browser.
   - Enter the name of the YouTube channel in the input form.
   - Click **Submit** to retrieve the channel’s video data and download the Excel file.

## API Usage
This application interacts with the YouTube Data API v3. The following endpoints are used:
- **`channels().list`**: Retrieves basic statistics about the channel.
- **`playlistItems().list`**: Extracts video IDs from the channel’s uploaded playlist.
- **`videos().list`**: Gathers video-specific data such as views, likes, comments, etc.

### Sample Excel Output:
A sample Excel file would contain columns like:
- Video URL
- Title
- Description
- Published Date
- Views, Likes, Comments
- Duration
- Course URL (if applicable)

## Future Improvements
- Allow users to search for any YouTube channel dynamically via the API, removing the need for predefined channel IDs.
- Provide options for filtering data (e.g., videos uploaded in the last 30 days, videos with over 1 million views).
- Add pagination support for channels with large numbers of videos.

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.

---

Let me know if you need further adjustments!
