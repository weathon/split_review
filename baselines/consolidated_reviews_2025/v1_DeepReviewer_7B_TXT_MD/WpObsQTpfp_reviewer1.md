### Summary

The paper introduces a large-scale image-text dataset, generated using the LLaMA-3-powered Llava model, to enhance vision-language models. The authors use a two-stage training process with LLaVA-1.5-LLaMA3-8B model on DataComp-1B dataset. The resulting dataset, Recap-DataComp-1B, is shown to improve performance on image-text retrieval and text-to-image generation tasks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed dataset is large-scale and well-curated.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other datasets, such as ShareGPT4V and ShareLLava, which also utilize LLaVA-1.5-LLaMA3-8B for generating image-text datasets. A comparison with these datasets would provide a clearer understanding of the unique contributions of the proposed dataset.
2. The paper does not include a comparison with other captioning models, such as BLIP-2 and InstructBLIP. Including these models would help to better understand the performance of the proposed dataset when used with different captioning architectures.
3. The paper does not provide a detailed analysis of the types of errors present in the generated captions. A detailed error analysis would help to understand the limitations of the proposed dataset and identify areas for improvement.

### Suggestions

The paper would significantly benefit from a more thorough comparison with existing datasets that also leverage LLaVA-1.5-LLaMA3-8B for caption generation. Specifically, a direct comparison with datasets like ShareGPT4V and ShareLLaVA is crucial. This comparison should not only focus on quantitative metrics such as image-text similarity and retrieval performance, but also on qualitative aspects like the diversity of generated captions and the presence of hallucinations. For instance, the authors could evaluate the performance of models trained on their dataset and these other datasets on a common benchmark, such as a zero-shot image retrieval task using a held-out set of images. This would provide a more robust understanding of the dataset's strengths and weaknesses relative to existing resources. Furthermore, it would be beneficial to analyze the types of errors that each dataset produces, such as the frequency of object hallucinations or the presence of inconsistent descriptions, to better understand the trade-offs involved in using each dataset.

In addition to comparing with other datasets, the paper should also explore the performance of the proposed dataset when used with different captioning models. While the authors have used LLaVA-1.5-LLaMA3-8B, it is important to evaluate the dataset's effectiveness with other architectures, such as BLIP-2 and InstructBLIP. This would help to determine the dataset's generalizability and identify any architectural biases. For example, the authors could train models using the proposed dataset and compare their performance on image-text retrieval and text-to-image generation tasks. They could also analyze the types of errors that each model makes, such as the frequency of incorrect object attributes or the presence of inconsistent relationships between objects. This would provide a more comprehensive understanding of the dataset's strengths and weaknesses and help to identify areas for improvement. Furthermore, it would be beneficial to explore the impact of different training strategies, such as varying the amount of training data or using different optimization algorithms, to determine the optimal settings for each model.

Finally, the paper needs a more detailed analysis of the types of errors present in the generated captions. This analysis should go beyond simple quantitative metrics and delve into the qualitative aspects of the captions. For example, the authors could categorize the errors into different types, such as object hallucinations, attribute errors, and relationship errors. They could then analyze the frequency of each type of error and identify any patterns or trends. This would help to understand the limitations of the proposed dataset and identify areas for improvement. For instance, if the dataset is found to be prone to object hallucinations, the authors could explore techniques to mitigate this issue, such as using a more robust captioning model or incorporating additional constraints into the training process. This would lead to a more comprehensive understanding of the dataset's limitations and provide valuable insights for future research.

### Questions

1. Could you provide a comparison of the proposed dataset with other datasets, such as ShareGPT4V and ShareLLava, to highlight its unique contributions?
2. Could you include a comparison with other captioning models, such as BLIP-2 and InstructBLIP, to demonstrate the dataset's effectiveness with different architectures?
3. Could you provide a detailed analysis of the types of errors present in the generated captions to better understand the dataset's limitations?

### Rating

5

### Confidence

4

**********
