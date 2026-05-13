# Dynamic Noise Preference Optimization for LLM Self-Improvement via Synthetic Data

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Although LLMs have achieved significant success, their reliance on large volumes of human-annotated data has limited their potential for further scaling. In this situation, utilizing self-generated synthetic data has become crucial for fine-tuning LLMs without extensive human annotation. However, current methods often fail to ensure consistent improvements across iterations, with performance stagnating after only minimal updates. To overcome these challenges, we introduce Dynamic Noise Preference Optimization (DNPO). DNPO employs a dynamic sample labeling mechanism to construct preference pairs for training and introduces controlled, trainable noise into the preference optimization process. Our approach effectively prevents stagnation and enables continuous improvement. In experiments with Zephyr-7B, DNPO consistently outperforms existing methods, showing an average performance boost of 2.6\% across multiple benchmarks. 
Additionally, DNPO shows a significant improvement in model-generated data quality, with a 29.4\% win-loss rate gap compared to the baseline in GPT-4 evaluations. This highlights its effectiveness in enhancing model performance through iterative refinement.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper explores an approach that uses synthetic data to help train a LLM.  The authors argue that human annotated data is both expensive and noisy, and sometimes nosier than generated data.  As such, they use a LLM to help score generated vs human samples.  In addition, to help promote continuous improvement, the authors add additional noise to further boost performance.

### Strengths
1. The topic addressed is both important and timely
2. The solution proposed is intuitive, and makes sense
3. The specific implementation seemingly differs from some prior work on this same task

### Weaknesses
 1. The authors only evaluate using a single architecture, and, thus, we don't know if the proposed improvements are only specific to this architecture.

2. The DNPO approach is quite similar to those in LNL, e.g., UNICON [A].  Whether the human or generated sample is the best label can also be framed from an LNL perspective.  As such, the contribution here can be argued as a simple application of this known solution.

3. Adding noise has some similarity to both masked language modeling and methods like excitation backprop [B] or self challenging [C].  While the proposed approach is seemingly different, it isn't clear if those differences are important

4. The gains are seemingly small enough that I would be concerned about their statistical significance.  The authors should provide a statistical test or even just error bars to alleviate this issue

5. The use of a LLM to evaluate the quality of the annotations is completely unconvincing.  One could argue that these language models are simply going to learn similar features, so all this test is doing is validating that this data is generated rather than that it is of a higher quality.

6. The authors cite several prior works that address the same task, but the authors do not compare against most of them.  As such, it isn't clear that the gains reported are significant in comparison to related work.

### Questions
Unfortunately I cannot shortlist my weaknesses to fewer questions.  Each of them would have to be addressed for me to significantly raise my score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the author intends to leverage the generated data to improve the performance of LLM. 
Some assumptions are not well verified or have some conflicts.

### Strengths
The main idea is easy to follow. 
The synthetic data is good to use. 
The task on boosting LM without human annotations is good for the community to explore.

### Weaknesses
My main concerns are that some claims are not verified and ambiguous.

1. Some claims contain conflicts.
- "Is human-annotated data truly better? "
The author said that " around 30% of the generated data is of equal or higher quality compared to the human-annotated data."
More fairly,  according to the number in Figure 1, we also could say that around 80% of the real data is of equal or higher quality compared to the human-annotated data.
So human-annotated data is truly better than generated data.

- Only using GPT4o-mini as the data quality metric is questionable.
I think it would be better to use a fused metric with SSIM, FID and manual check.

- “stagnation” is ambigous.
Figure 2, I only can see the model overfits the generated data.
I think "overfitting" is better than using "stagnation".
How about more generated data, since the data generation is free from the human annotation?
Will the model still overfit the generated data?

2. Ablation studies.
The author claims that "the lack of variation in generated data across iterations, leading to stagnation during model updates."
One simple method is using the generative model for online data generation.

3. Contribution-1 Dynamic sample labeling (DSL)  is incremental.
DSL seems to be a simple filtering process?
I do not see any technical contribution. Similar filterring process has been widely used in the model trainning, such as BLIP.

4. The motivation of  Contribution-2 Noise preference optimization (NPO) is not well-proved.
Figure 10 is not supposed to be better than the existing methods in Figure 2.
I think the data distribution only shows the style similarity but does not indicate the good data for training.
Indeed, Figure 10 is simmilar to Figure 2, but the figure 10 shows more generated data.

### Questions
Please see the points in Weakness.

1. Some claims contain conflicts. Please explain. 

2. Ablation studies are missing. 

3. Contribution-1 is incremental. 

4.The motivation of  Contribution-2 Noise preference optimization (NPO) is not well-proved.
Indeed, figure 10 is simmilar to Figure 2, but the figure 10 shows more generated data.

### Soundness
2

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
2

### Summary
This paper attmpts to improve the LLM using generated data, and propose a method named DNPO. The authors challenge the assumption that the human-annotated data is superior than the generated data, and devise a dynamic smaple labeling strategy to pick both the human-annotated data and the synthesic data for LLM tuning. Ana an noise preference optimization is proposed to utilize the picked data from DSL. Experiment results show that the proposed method can attain better performance than SPIN.

### Strengths
using fake data to improve LLM is an interesting  and study-worhty problem.
a clear motivation is presented

### Weaknesses
1, Dynamic sampling labeling requires an "more powerful evaluation model"  to evaluate the human-generated data and synthesic data,   does this evaluation nedd to be superiror than the LLM model to be improved?  If yes, why do you not directly tune the evaluation model? If no, how do you ensure the given evaluation is credible and indeed pick more valuable data to fine-tune the LLM? 

2, SPIN adopts 50K prompts from UltraChat for evaluation, while this paper only picks 20K,  why do not align the amount?

3,  How the amount of the synthesic data effects the final results, I did not observe any discussion regarding this quesion.

### Questions
Figure 2 x and y-axis are both not clear for me

### Soundness
3

### Presentation
2

### Contribution
3
