# VisionScriptBot
A telegram bot that uses Google's Gemini Pro Vision API 

## Gemini API 
VisionScriptBot uses Google new [Gemini Pro Model](https://ai.google.dev/docs) . 

[Gemini](https://deepmind.google/technologies/gemini/) is Google's latest family of large language models. This site contains all the info you need to start building applications with Gemini.

You need Google Api key 🔐 for Gemini to run this model. 
Get your api key from 
https://makersuite.google.com/app/apikey


Google's Python SDK for the Gemini API, is contained in the google-generativeai package. Install the dependency using pip:


```bash
pip install -q -U google-generativeai
```

for complete guide [refer](https://ai.google.dev/tutorials/python_quickstart)


### Gemini Vision Pro

Gemini Pro Vision is a Gemini large language vision model that understands input from text and visual modalities (image and video) in addition to text to generate relevant text responses.

Gemini Pro Vision is a foundation model that performs well at a variety of multimodal tasks such as visual understanding, classification, summarization, and creating content from image and video. It's adept at processing visual and text inputs such as photographs, documents, infographics, and screenshots.


#### Use cases

1. Visual information seeking: Use external knowledge combined with information extracted from the input image or video to answer questions.

1. Object recognition: Answer questions related to fine-grained identification of the objects in images and videos.

1. Digital content understanding: Answer questions and extract information from visual content like infographics, charts, figures, tables, and web pages.

1. Structured content generation: Generate responses based on multimodal inputs in formats like HTML and JSON.

1. Captioning and description: Generate descriptions of images and videos with varying levels of details.

1. Reasoning: Compositionally infer new information without memorization or retrieval.


## Demo

![](https://github.com/nuhmanpk/VisionScriptBot/blob/main/demos/Screenshot_20231230-115838.png)
