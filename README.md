# RelatedPics
**A simple Python program interpreting the [PixaBay API](https://pixabay.com/api/docs/) and the [Microsoft Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)**


*the Azure code is from [here](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/python-sdk)*

## Before you start
* make sure you have git installed [download git](https://git-scm.com/)
* make sure you have python installed [download it](https://www.python.org/downloads/) (this requires Python 3.0 or higher)
### Get your API keys
#### Azure

##### Create the service
1. Go to the [Microsoft Azure portal](https://portal.azure.com/#home)

<img src="https://files.catbox.moe/x3s2pk.jpeg" alt="search bar" width="700"/>


2. In the search bar search for computer vision
<img src="https://files.catbox.moe/wmonds.jpeg" alt="search bar" width="700"/>

3. Click on "Computer vision" from the Marketplace section
4. Fill in the details and select the free pricing tier (you also can select the S1 tier, but for our purposes, the free one will be enough).
<img src="https://files.catbox.moe/g68die.jpeg" alt="search bar" width="700"/>
5. Then just hit the Create button and now we're done creating the Cognitive service.

##### Getting the API key and the endpoint URL
1. From the Azure Portal sidebar, go to "All resources"

2. Then go to the resource you just created and select "Quick start"
<img src="https://files.catbox.moe/04gbl1.jpeg" alt="search bar" width="700"/>

#### Azure
To get your Pixabay API key, go to the [API documentation page](https://pixabay.com/api/docs/) [requires sign-in first] and copy the code from the page
![get Pixabay API key](https://files.catbox.moe/5vwn1n.png)
## Setup

1. In the Terminal or CMD, clone the repo with ```git clone https://github.com/filiptronicek/related-pics.git```
2. Set the environment variables `COMPUTER_VISION_SUBSCRIPTION_KEY`, `COMPUTER_VISION_ENDPOINT` and `PIXABAY_API_KEY` with ```setx COMPUTER_VISION_SUBSCRIPTION_KEY "your-key"```
3. Start the script with `python main.py`
