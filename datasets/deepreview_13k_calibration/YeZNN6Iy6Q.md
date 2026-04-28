# Effective Text-to-Image Alignment with Quality Aware Pair Ranking

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5

## Abstract
Fine-tuning techniques such as Reinforcement Learning with Human Feedback (RLHF) and Direct Preference Optimization (DPO) allow us to steer Large Language Models (LLMs) to be align better with human preferences. Alignment is equally important in text-to-image generation. Recent adoption of DPO, specifically Diffusion-DPO, for Text-to-Image (T2I) diffusion models has proven to work effectively in improving visual appeal and prompt-image alignment. The mentioned works fine-tune on Pick-a-Pic dataset, consisting of approximately one million image preference pairs, collected via crowdsourcing at scale. However, do all preference pairs contribute equally to alignment fine-tuning? Preferences can be subjective at times and may not always translate into effectively aligning the model. In this work, we investigate the above-mentioned question. We develop a quality metric to rank image preference pairs and achieve effective Diffusion-DPO-based alignment fine-tuning. We show that the SD-1.5 and SDXL models fine-tuned using the top 5.33\% of the data perform better both quantitatively and qualitatively than the models fine-tuned on the full dataset. The code is available at https://anonymous.4open.science/r/DPO-QSD-28D7/README.md

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new approach to improve text-to-image alignment in diffusion models by introducing a quality-aware pair ranking (QSD) mechanism. The key idea is to rank image preference pairs based on an AI-generated quality metric, allowing for more effective fine-tuning with higher-quality samples. Experiments indicate that using only the top-ranked 5.33% of preference pairs results in significant performance improvements, both quantitatively and qualitatively, over models trained with the full dataset. The authors suggest that this ranking approach enables more efficient model alignment with human preferences.

### Strengths
1. The proposed approach is straightforward and does not require complex architectural changes, making it accessible for integration with existing systems.
2. The QSD ranking approach demonstrates significant improvement in both alignment and training efficiency, as evidenced by quantitative and qualitative metrics.

### Weaknesses
1. My main concern is that this method relies heavily on clear preference pairs, or “easy samples.” While this strategy effectively avoids the noise introduced by pairs with similar quality scores in the dataset, it is highly likely to lead to overfitting on easily distinguishable image pairs, thereby limiting the model’s generalization ability in practical applications. This issue has been discussed in many papers [1, 2, 3]. Specifically:
a. All experiments and evaluations are conducted on the Pick-a-Pic dataset, raising concerns about the model's generalizability.
b. From Figures 6 and 7, it is evident that QSD-selected pairs tend to have clear differences in content but may lack nuanced human preference subtleties. Ignoring this data could prevent the model from learning finer distinctions in preference. It is recommended that the authors validate QSD’s effectiveness on a more granular dataset.
c. Real-world applications require models to handle various complex and ambiguous inputs. By entirely excluding such pairs from training, the model may perform poorly when encountering similarly ambiguous inputs in practical settings.
2. There are indications of noisy data in the Pick-a-Pic dataset. For example, in Figure 6 (row 1, column 3), a winning image does not seem to align well with the prompt, raising questions about data quality. It would be beneficial to conduct an ablation study where QSD filters out low-quality pairs to assess its effectiveness in reducing noise for DPO training.
3. The QSD method relies on filtering existing datasets of image preference pairs, which are costly to construct. This limitation restricts the method’s practical applicability. The authors are encouraged to explore automated pipelines to create high-quality preference data at scale.
4. More detailed explanations of how QSD ranks pairs and why specific thresholds (such as the top 5.33%) were chosen would improve readability and comprehension.
5. It would be beneficial to include a discussion of the limitations of the proposed approach and potential directions for future development.

### Questions
1. Why are Figures 5(a) and 5(b) identical? Please verify the caption in Figure 5(a) which reads “SD1.5-DPO vs SD1.5-DPO.”
2. In Figure 6, row 1, column 3, the ground truth (GT) label for the winning image seems misaligned with the prompt. Instead of focusing solely on high-quality pairs, would it be more beneficial to filter out noisy data to enhance DPO training?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a data curation method for DPO based preference optimization for text-to-image models. The main idea is to decide how useful a certain preference is using the proposed quality metric. The proposed quality metric is basically a product of the score for the winning sample, and the inverse (1-x) for the losing sample. Performing LoRA fine tuning with Diffusion-DPO (or its variants) on both SD1.5 and SDXL improves metrics on several evaluation setups (human preference reward model evaluations and user studies).

### Strengths
The biggest strength of the paper in my view is that it starts the discussion on data quality for preference datasets of T2I models. While open-source datasets are not widely available, filtering existing datasets to get much better data would be essential to improve the results. 

In that context, the results obtained in the paper are quite compelling. The quality metric proposed here is quite simple/straightforward, yet provides consistent gains across different DPO strategies (e.g. ORPO etc.)

### Weaknesses
A major "weakness" that can be pointed to this paper is that the contribution is somewhat basic and limited -> i.e introduce a quality metric to rank pairs and select the top ranked papers to perform Diffusion-DPO with LoRA fine-tuning. To that extent, there's limited contribution, and I would love to have seen more insights for curating future preference datasets.  

I would have also loved to have seen some more insight into whether the images are an issue, or are the labels wrongly assigned by the annotators? For instance, if we were to relabel the Pick-a-Pic dataset using HPSv2, how does the resulting DPO process look like (the kinds of experiments in Fig.6 and Tab. 2 in the Diffusion-DPO paper). There's also one qualitative figure showing "good pairs" and "bad pairs", but something more concrete/quantitative would also provide a lot more support. 

In general, I think the paper is touching upon a crucial aspect of preference datasets for (Diffusion) DPO, and is valuable, but I would really like to see some more analyses and insights before confidently recommending acceptance.

### Questions
I am mostly confused by the results in Tab. 3 and would like the authors to clarify the details. The first question is why do different methods have such differing % of samples used? For HPSv2 and PickScore it's 5.33% while for Aesthetic predictor it's 16% and with ImageReward it's all the samples (i.e no filtering)? Couldn't the same number of samples be used for all the scoring methods to keep it more balanced? Especially when no filtering is applied (i.e the ImageReward case), I am not sure what value is being added by the scoring method at all?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method to enhance text-to-image diffusion models' alignment with human preferences by ranking image pairs with a quality metric. It shows that fine-tuning on just 5.33% of the best-ranked pairs from the Pick-a-Pic dataset outperforms models fine-tuned on the full dataset, demonstrating efficiency and robustness across various methods.

### Strengths
1. The paper demonstrates that by using a quality-aware pair ranking method, the alignment of T2I models with human preferences is improved, leading to better quantitative and qualitative results.
2. A key advantage is the dramatic increase in fine-tuning efficiency. The authors show that their models can achieve superior performance using only a small fraction (5.33%) of the full dataset, indicating a substantial reduction in computational resources and time.

### Weaknesses
1. Where did the 5.33% setting come from? Why 5.33%?
2. The paper is more of an experimental report, with its main contribution being the application of a quality metric rather than a significant theoretical or methodological innovation.
3. There's a risk that the model may overfit to the Pick-a-Pic dataset, and its generalizability to other datasets or domains is not fully explored.
4. The approach heavily depends on AI reward models, which, if biased or inaccurate, could negatively affect the fine-tuned T2I models' alignment with genuine human preferences.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a sample selection approach specifically designed for the training of text-to-image generation models. Through a set of conducted experiments, the method has shown to be beneficial in improving the training process of such models. The results indicate that the proposed selection technique can contribute to the efficiency and quality of the generated images. Furthermore, the data generated and used in this study has been made available to the community, which may be of use for other researchers working in the text-to-image generation domain.

### Strengths
1. The paper addresses a relatively novel topic in the field of image generation. 
2. It presents a study that has conducted a series of experiments to explore and validate the proposed approach.

### Weaknesses
1. The paper employs the HPSv2 to filter samples in a computational study. The novelty of the approach is quite limited. Additionally, the paper notes the potential bias inherent in using HPSv2 as the sole scoring metric and recommends incorporating a variety of indicators for a more balanced evaluation. The results tabulated in the paper suggest that the HPSv2 metric shows a more pronounced improvement compared to other metrics when contrasted with the baseline model. Thus, the authors emphasize the necessity for a more extensive experimental validation to comprehensively confirm the superiority of the QSD method.

2. This paper presents a study focused on the quality of a model trained on a single dataset, which limits the generalizability of the findings as it does not extend the validation to other datasets. The lack of cross-dataset testing makes it challenging to assert the model’s ability to generalize its quality performance. 

3. A recommendation is made to include a comparative experiment where a subset of the full dataset, randomly sampled to match the size of the QSD, is used for benchmarking purposes. 

4. Furthermore, the organization and layout of the paper could be improved; for instance, the placement of Figure 3 and Figure 4 appears to be inappropriate, and the design of the tables is somewhat incomplete, which could benefit from a more refined presentation.

### Questions
Please refer to weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
