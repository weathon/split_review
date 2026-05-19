### Summary

This paper proposes a unified training framework to learn from both 2D and 3D perceptual data as well as standard image-text pairs. The authors first develop a large-scale language-image pretraining dataset for 2D and 3D, called LV3D. Then, they train a MLLM on LV3D as a single “next token prediction” task, called Cube-LLM. The authors demonstrate that pure data scaling can achieve their goal without any 3D specific architectural design or training objective. The experiments on outdoor benchmarks demonstrate that Cube-LLM significantly outperforms existing baselines by 21.3 points of AP_BEV on the Ttc dataset for 3D grounded reasoning and 17.7 points on the DLM dataset for complex reasoning about driving scenarios, respectively.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors propose a unified training framework to learn from both 2D and 3D perceptual data as well as standard image-text pairs. The authors first develop a large-scale language-image pretraining dataset for 2D and 3D, called LV3D. Then, they train a MLLM on LV3D as a single “next token prediction” task, called Cube-LLM. The authors demonstrate that pure data scaling can achieve their goal without any 3D specific architectural design or training objective. 
2. The experiments on outdoor benchmarks demonstrate that Cube-LLM significantly outperforms existing baselines by 21.3 points of AP_BEV on the Ttc dataset for 3D grounded reasoning and 17.7 points on the DLM dataset for complex reasoning about driving scenarios, respectively. 
3. The authors show that Cube-LLM performs the state-of-the-art in 2D referring expression comprehension, achieving the average score of 87.0 on refCOCO+/g.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that they show that Cube-LLM exhibits intriguing properties similar to LLMs: (1) Cube-LLM can apply chain-of-thought prompting to improve 3D understanding from 2D context information. (2) Cube-LLM can follow complex and diverse instructions and adapt to versatile input and output formats. (3) Cube-LLM can be visually prompted such as 2D box or a set of candidate 3D boxes from specialists. However, the authors do not provide sufficient evidence to support these claims. Specifically, the paper lacks quantitative evaluations demonstrating the effectiveness of chain-of-thought prompting for 3D understanding. The claim about following complex instructions is not backed by specific examples or metrics showing the model's ability to handle diverse input/output formats beyond standard 2D and 3D bounding boxes. The visual prompting claim also needs more rigorous evaluation, such as showing performance gains when using 2D boxes or 3D candidate boxes from specialists compared to the model's performance without such prompts.
2. The authors claim that Cube-LLM shows remarkable improvement with data-scaling in both 2D and 3D, for indoor and outdoor scene grounding as well as complex reasoning tasks such as QA in driving scenarios. However, the authors do not provide sufficient evidence to support this claim. The paper does not include ablation studies that isolate the impact of data scaling on the model's performance. It is unclear whether the performance gains are solely due to the increased data volume or other factors such as the specific composition of the dataset. Furthermore, the paper lacks a detailed analysis of the model's performance on indoor vs. outdoor scenes, making it difficult to assess the claim of improvement in both settings.
3. The authors claim that the authors show qualitative results in 3D grounding in non-driving scenes (Fig. 2). However, the authors do not provide sufficient qualitative results to support this claim. The paper only presents a few qualitative examples, which are insufficient to demonstrate the model's generalization ability across diverse non-driving scenes. A more comprehensive set of qualitative results, including failure cases, would be necessary to validate this claim.

### Suggestions

To strengthen the claims regarding Cube-LLM's LLM-like properties, the authors should conduct more rigorous evaluations. For the chain-of-thought prompting, they should compare the model's performance with and without this prompting strategy on 3D understanding tasks, using metrics that specifically measure the quality of the reasoning process. For example, they could use metrics that evaluate the correctness of intermediate steps in the reasoning chain. To support the claim about following complex instructions, the authors should provide examples of diverse input/output formats that the model can handle, along with quantitative metrics that measure the model's accuracy on these tasks. This could include tasks that require the model to output different types of information, such as object attributes, spatial relationships, or even textual descriptions. For the visual prompting claim, the authors should conduct experiments that compare the model's performance with and without visual prompts, such as 2D boxes or 3D candidate boxes, and report the performance gains achieved by using these prompts. These experiments should be conducted on a variety of datasets to ensure the robustness of the results.

To validate the claim about the impact of data scaling, the authors should perform ablation studies that systematically vary the amount of training data and analyze the resulting performance changes. This would help to isolate the effect of data scaling from other factors. The authors should also provide a detailed analysis of the model's performance on indoor and outdoor scenes separately, using metrics that are appropriate for each setting. This analysis should include a comparison of the model's performance on different types of indoor and outdoor scenes to identify any potential biases or limitations. Furthermore, the authors should investigate the impact of different data compositions on the model's performance, such as the proportion of 2D and 3D data, and the diversity of the data. This would help to understand the optimal data composition for training Cube-LLM.

Finally, to support the claim about qualitative results in 3D grounding, the authors should provide a more comprehensive set of qualitative examples, including both successful and failure cases. These examples should cover a wide range of non-driving scenes, such as indoor scenes with different object arrangements and outdoor scenes with varying lighting conditions. The authors should also provide a detailed analysis of the failure cases, explaining the reasons for the model's errors. This would help to identify the limitations of the model and guide future research directions. The qualitative results should be presented in a clear and organized manner, with detailed captions that explain the context of each example.

### Questions

1. The authors claim that they show that Cube-LLM exhibits intriguing properties similar to LLMs: (1) Cube-LLM can apply chain-of-thought prompting to improve 3D understanding from 2D context information. (2) Cube-LLM can follow complex and diverse instructions and adapt to versatile input and output formats. (3) Cube-LLM can be visually prompted such as 2D box or a set of candidate 3D boxes from specialists. However, the authors do not provide sufficient evidence to support these claims. 
2. The authors claim that Cube-LLM shows remarkable improvement with data-scaling in both 2D and 3D, for indoor and outdoor scene grounding as well as complex reasoning tasks such as QA in driving scenarios. However, the authors do not provide sufficient evidence to support this claim. 
3. The authors claim that the authors show qualitative results in 3D grounding in non-driving scenes (Fig. 2). However, the authors do not provide sufficient qualitative results to support this claim.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
