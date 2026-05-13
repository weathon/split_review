# NutriBench: A Dataset for Evaluating Large Language Models in Nutrition Estimation from Meal Descriptions

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Accurate nutrition estimation helps people make informed dietary choices and is essential in the prevention of serious health complications. We present \nutri, the first publicly available natural language meal description nutrition benchmark. \nutri~consists of 11,857 meal descriptions generated from real-world global dietary intake data. The data is human-verified and annotated with macro-nutrient labels, including carbohydrates, proteins, fats, and calories. We conduct an extensive evaluation of \nutri\ on the task of carbohydrate estimation, testing twelve leading Large Language Models (LLMs), including GPT-4o, Llama3.1, Qwen2, Gemma2, and OpenBioLLM models, using standard, Chain-of-Thought and Retrieval-Augmented Generation strategies. Additionally, we present a study involving professional nutritionists, finding that LLMs can provide more accurate and faster estimates. Finally, we perform a real-world risk assessment by simulating the effect of carbohydrate predictions on the blood glucose levels of individuals with diabetes. Our work highlights the opportunities and challenges of using LLMs for nutrition estimation, demonstrating their potential to aid professionals and laypersons and improve health outcomes.
Our benchmark is publicly available at: \url{https://mehak126.io/nutribench.html}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents NUTRIBENCH, a new benchmark dataset designed to evaluate LLMs on nutrition estimation from natural language meal descriptions. The dataset includes 11,857 meal descriptions annotated with macronutrient labels (carbohydrates, proteins, fats, and calories), generated from global dietary intake data. The authors assess twelve LLMs.

### Strengths
- Nutribench is the first of its kind for the task of macronutrient estimation from the textual description of meals. 
- The paper benchmarks multiple LLMs and also explores/compares multiple prompting strategies. 
- The authors conduct an evaluation involving nutritionists as well. 
- The authors do a comprehensive analysis of performance across different dimensions.

### Weaknesses
 - The authors have relied on GPT4o to generate meal descriptions. There is a concern with this. Were all of the outputs by GPT4o verified by humans? 
- The fine-tuning experiment with Gemma2-27B shows improvements but does not address whether larger or different models would perform similarly with fine-tuning.
- The choice of specific prompting methods (e.g., why Chain-of-Thought outperforms other methods) should be discussed well.
- Although the paper mentions about the performance disparities across cultural diets, it does not explicitly address if these are due to model biases or data representation gaps or any unique characteristics of the specific foods.

### Questions
- What measures are taken to verify the nutritional information accuracy of each meal description, especially considering human verification only involves a single author?
- Could you provide additional details on how you mapped food quantities to everyday serving sizes? For instance, how does the rule-based algorithm handle ambiguous measurements?
- How do you explain the higher error rates in carbohydrate estimation for high-carbohydrate foods? Does the model struggle with certain food types or serving sizes?
- What might be the underlying causes for cultural discrepancies in model performance, particularly for countries like Sri Lanka with higher MAE?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study presented NutriBench, a natural language meal description dataset labeled with macronutrient and calorie estimates. It evaluated 12 LLMs covering both open and closed source models with different prompting strategies on carbohydrate estimation. It also conducted a study with 3 nutritionists to obtain carbohydrate estimates on a sample of meal descriptions. Through a real-world risk assessment by simulating the effect of carbohydrate estimates on the blood glucose levels of Type 1 diabetes patiens, it found that LLM can help Type 1 diabetes patients maintain their blood glucose within safe limits.

### Strengths
(1) This study worked on an important issue which may influence diabetes management.

(2) Most of the writings are clear.

(3) In addition to a benchmark, this study also provided a preliminary experiments comparing LLMs with human experts. It also showed how it might be applied to real-world management via a case study.

### Weaknesses
 (1) The study might be much improved if it could provide more insights into the success and failure cases of the LLMs on the carbohydrate estimation task. When LLMs made wrong estimations, what were those mistakes? Was it because LLMs did not have the information, or it was more like a math operation issue. To me, it is unclear what capabilities of LLMs did this study intend to find out. If it is just for evaluating LLMs for carbohydrate estimation, the research contribution might be limited. It would be better if the authors could further explain how the findings of this study may inspire future works. Why is it different from other LLM benchmark papers? 

(2) The study should disclose hyperpoparameter settings in detail.

### Questions
Questions:

(1) NutriBench consists of 11,858 meal descriptions. Was the human verification applied to all of them?

(2) It appears that human verification might induce subjective biases. Take the pizza case as an example, why should we update "a tasty medium crust pepperoni pizza" to "a piece of tasty medium crust pepperoni pizza"?

(3) Is the benchmark robust and reproducible? Even though the temperature can be set 0 to obtain more deterministic responses, it is uncertain whether the responses will be reproducible. It would be better to include additional experiments for this concern. 

(4) Does the prompt have to be strictly formulated to produce the results? Would paraphrasing the prompt significantly change the results?

(5) Would there be any biases when the data generator and carbohydrate estimator are identical? In this case, both are GPT-4o-mini.

(6) What is the x-axis in Figure 6?

(7) In the simulation experiment, it seems that the performance of different nutritionist varies significantly. Why is that?

(8) According to Figure 2, the human nutritionist performed worse than a lot of LLMs. When human made mistakes, what were those mistakes? Did LLMs perform better just because they held more knowledge? If each food is associated with a pre-defined value, why can't nutritionists looked those up if they were not sure of the knowledge?

(9) The authors discussed that previous benchmarks mainly focused on using images. I wonder whether it is feasible to caption the images from these datasets and expand the existing one. Additionally, why not caption the images instead of constructing a benchmark from the scratch?

Minor:

(1) It would be better to use verb tense consistently.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a benchmark called NutriBench, which includes 11,857 meal descriptions derived from real-world global dietary intake data. It employs Chain of Thought (CoT) and Retrieval-Augmented Generation (RAG) techniques to tackle the carbohydrate estimation task and evaluates twelve large language models (LLMs), such as GPT-4o and Llama 3.1. Ultimately, a real-world carbohydrate prediction task is conducted. The results demonstrate a significant improvement in both the accuracy and speed of carbohydrate estimation compared to traditional nutritionists.

### Strengths
1. Data Collection: This study gathers 11,857 meal descriptions from various countries. This approach enhances text flexibility compared to traditional tabular data and addresses the challenges of acquiring image data.
2. Model Evaluation: The research evaluates the carbohydrate prediction capabilities of different large language models (LLMs). The results show that these models outperform nutritionists in both prediction speed and accuracy.
3. Social Influence: The paper conducts a real-world risk assessment by simulating how carbohydrate predictions affect blood glucose levels in individuals with diabetes. This demonstrates the potential positive impact of LLMs on public health.

### Weaknesses
1. Limited downstream tasks: the paper only focuses on the carbohydrate prediction task. More downstream tasks can be performed, e.g., protein prediction, etc.
2. Over-reliance on description quality: the prediction performance generated by LLMs relies heavily on the quality (comprehensiveness, accuracy, etc) of description data.

### Questions
More downstream tasks and comprehensive analyses on nutrition can be performed to generate more informative insights, compared to just providing carbohydrate predictions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper describes a new dataset, NutriBench, that contains over 10,000 synthetically generated natural language meal descriptions and corresponding macronutrients from matching foods in the Food Data Central database. They run experiments with 12 open and proprietary large language models, including varients of GPT, Qwen, and Llama on the task of carbohydrate prediction. They found that GPT-4o with Chain-of-Thought prompting resulted in the highest accuracy and response rate.

### Strengths
The greatest strength is the public release of the NutriBench dataset. Particularly impressive is that the dataset is based on real meals that people across 11 different countries eat. Another strength is the extensive experiments that were run, testing 12 LLMs, using three prompting strategies, comparing to nutritionists, and simulating the effect of carbohydrate predictions on blood glucose levels of individuals with diabetes. The takeaways for which LLMs perform best under which conditions (i.e., prompt, natural vs metric serving size, and diet/country) are important for researchers in this area. The real-world risk assessment with the Tidepool simulation of blood sugar levels is interesting, as are the LLM prompts in the appendix. Finally, this is an important problem with broad societal impacts—diet tracking is challenging, and finding ways to reduce user burden is critical for continued usage, which will help with obesity, diabetes, heart disease, and many other health conditions.

### Weaknesses
The biggest strength is the database, but the data that will be released and was included in the supplementary material contains only the natural language meal descriptions, no Food Data Central entities or their nutrition information. In addition, the only task was carbohydrate prediction, and the authors mention that the dataset contains only macronutrient information, but an LLM nutritionist should be able to predict protein and fat as well, and micronutrients as very important too. 11,857 meal descriptions is a small number, but is reasonable given they are human-verified. Another major weakness is the study in section 6 comparing LLMs to human nutritionists. It is understandable that human experts are slower, but instructing nutritionists not to search the web for carbohydrate estimates and then claiming that LLMs are more accurate seems quite problematic and results in a very misleading conclusion. Nutritionists do their job by using tools and resources. You can’t get an accurate measure of their ability to estimate carbohydrates if you take away the tools they use in the real world. The only actual takeaway here is that LLMs are faster, which is obvious. I love this work and really wanted to accept this paper, but can’t justify it due to these weaknesses.

### Questions
•	Note that Answer Rate and RETRI-DB are used before they are defined—consider moving up the definitions to the first place these terms are used.
•	Consider explaining why you used generative AI to write the natural language meal descriptions instead of humans.
•	Were all the foods eaten by people in 11 countries in the USDA’s Food Data Central? I’m surprised you had full coverage of globally eaten meals just from the US food database.
•	Please fix the caption for Figures 4 and 5.
•	In section 5.2, you comment that LLM predictions are more accurate for individuals on a low-carb diet. However, aren’t people on a high-carb diet more likely to get diabetes?
•	In section 5.3, why did you use the Base prompting method instead of CoT to generate responses when you said yourself that CoT is more accurate?
•	In real life, when someone has diabetes, how do they dose their insulin typically? I’m guessing they’re not calculating their carbs every time they eat.
•	In Appendix B.2, a couple of the human-verified responses actually seemed worse to me, with misspellings and unnecessary food words added (“sandwich” to “biscuit”).
•	Why is your FDC database only 450K foods? Doesn’t it contain over 1.8M foods?

### Soundness
3

### Presentation
3

### Contribution
3
