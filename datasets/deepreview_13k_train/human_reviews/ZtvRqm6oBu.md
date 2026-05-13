# Applying Sparse Autoencoders to Unlearn Knowledge in Language Models

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
We investigate whether sparse autoencoders (SAEs) can be used to remove knowledge from language models. We use the biology subset of the Weapons of Mass Destruction Proxy dataset and test on the \gone and \gtwo language models. 
We demonstrate that individual interpretable biology-related SAE features can be used to unlearn a subset of WMDP-Bio questions with minimal side-effects in domains other than biology.
Our results suggest that negative scaling of feature activations is necessary and that zero ablating features is ineffective. 
We find that intervening using multiple SAE features simultaneously can unlearn multiple different topics, but with similar or larger unwanted side-effects than the existing Representation Misdirection for Unlearning technique. 
Current SAE quality or intervention techniques would need to improve to make SAE-based unlearning comparable to the existing fine-tuning based techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper uses sparse autoencoders to identify features related to biology, which they isolate and clamp down to unlearn on a subset of the WMDP dataset. They use two versions of gemma-2b-it, intervening at an intermediate layer on specific bio-related features. They find that such an intervention can be successful in unlearning, while adding relatively small loss on a generic text dataset.

### Strengths
I think applying SAEs to this task is useful – for us to do good unlearning we almost certainly want an interpretable method, so these are worthwhile first steps. I like the depth you went into in Section 3, as well as Figure 2. I think the methodology was clearly defined, as well as the metrics and tasks you were evaluating. I think there are some nice ablations as well, e.g., Section 4.2.

### Weaknesses
I think the messaging of the paper needs to change to increase the novelty by emphasizing how your work and existing work (RMU) differ. Specifically, how yours is more interpretable and why that’s a good thing. I know the latter is mentioned in the intro but that’s the most substantive discussion of this difference, which is the main reason right now people would want to use SAEs for unlearning.

I think the experiments section should include both gemma models. Relatedly, I think Figure 4 is weak and makes the results hard to interpret. I also don’t really know why the added loss would matter much when you show such a relatively large deterioration on MMLU.

I’d prefer you to show at least some results on even one other subset of WMDP just to see how this generalizes. I wonder if SAEs may be more helpful than fine-tuning if we are trying to unlearn a combination of separate tasks, e.g., both biology and chemistry.

Finally, there is a lack of a related work section, which I feel is necessary as I think you could better contextualize your, e.g., by further showing how people are currently using SAEs to adjust features.

### Questions
-	Why did you select the hyperparameters you did for the clamped feature activations (1x, 10x, 50x, etc.)? Same for RMU hyperparameters? Specifically, the layers.
-	Why did you use 300x in Figure 5 but not Figure 4?
-	On page 2, “We trained SAEs at several intermediate layers of the residual stream” – which layers? Sometimes you use layer 3, sometimes layer 9.
-	Why do you use gemma-2b-it for Section 3, but don’t present results for gemma-2b-it in the main body? There is a disconnect between this and Section 4, which uses gemma-2-2b-it.
-	On page 5, there are experiments mentioned but I’d like to see the results somewhere: “To investigate the importance of the particular feature that we selected, we performed the same ablation on a variety of features that activate on this prompt, chosen at random.”
-	Figure 1 feels bare. You could consider including some results in half of this figure or some examples on the bio WMDP subset so it is more tailored to your goal instead of a somewhat bare depiction of a SAE.

These did not affect my review, but some smaller things to note:

-	Could you use different symbols to represent the feature number and question? You use “#” for both feature number and question number (e.g., “feature #9163” and “question #841”), which I think is distracting.
-	In the conclusion you say intervening using “10-20” features – I would change it to 10 or 20 because you don’t use any intermediate values in the range.
-	On page 4, “The model still provides “A” as the correct answer with probably” -> “probability”
-	On page 6, I would explicitly define what $L0$ means in $L0\approx 59$ for readers are less familiar with SAEs.
-	Figure 5 you should use a different color for the random decoder vector as in Figure 4 you use that some color for representing a 20 feature intervention.
-	On page 8, you say “We propose four key directions for future research” but only provide three.

### Soundness
3

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
3

### Summary
This paper tests the use of sparse autoencoders (SAEs) for unlearning specific knowledge in LLMs, their application of interest is the biosecurity-related Weapons of Mass Destruction Proxy dataset. The authors selectively suppresses SAE features that are highly used by the WMDP dataset (i.e. figure 2). Experiments compare SAE-based unlearning with Representation Misdirection for Unlearning methods, they test accuracy and side effect on the OpenWebText dataset. The authors report effective unlearning with some success in minimizing side effects, though challenges remain with both interpretability and the general applicability of SAEs for unlearning.

### Strengths
* Unlearning
* Minimal side effects

### Weaknesses
 * Not concise: I still don't fully understand what a SAE is. The entire paper proposes a new methodological framework without a single math equation. It is very hard to follow and reads like a conversation between LLM software engineers moreso than a technical report on a new methodology.
* Plots everywhere: why is figure 10 cited an entire page before figure 2? The figures should be placed in close proximity to the text in which it is being discussed
* What causes the drop on OpenWebText? What datapoints do you lose performance on? How many datapoints do you misclassify? What type of questions are they?
* It might just be unlearning biology related content. There should be more focus on testing biology related content.

### Questions
Figure 2: the figure says it's a distribution, but it has counts on the y-axis. Also, it does not seem to be normalized per dataset, i.e. the OpenWebText is a lot smaller, why is that? Also, why is figure 2 on page 2 instead of next to the text it's mentioned in. Please fix that it makes it hard to follow the storyline.

"Interestingly, the model modified using RMU answers option “A” on 62% of questions,
compared to 25% for the base model." I dont understand what that means.

"2.4 HOW TO SELECT RELEVANT SAE FEATURES" by this point in the paper I still have no idea what a SAE feature is and this section is unintuitive to me. In general, until this point, the paper has been very verbose and has had limited conciseness.

Section 3:
The entire section has heavy use of DL/LLM lingo and explains the methodology using "math-intuition". This is, in fact, quite unintuitive to me. Please rewrite and be concise about the method you are proposing. I am sure you can do it in much less space.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the potential of using sparse autoencoders (SAEs) to remove specific types of knowledge from language models in an interpretable way. Specifically, it investigates whether SAEs can selectively "unlearn" harmful biology-related information from two language models, gemma-2b-it and gemma-2-2b-it, using a subset of Weapons of Mass Destruction Proxy dataset. The main findings suggest that adjusting (negatively scaling) certain biology-related feature activations is effective for unlearning this knowledge, whereas simply zeroing out features is not effective.

Key insights include:
1. Negative scaling of feature activations is necessary for unlearning specific topics, while zeroing features is ineffective.
2. Multiple SAE features can be manipulated simultaneously to unlearn several topics, but this method has side effects similar to, or greater than, those of the existing fine-tuning-based Representation Misdirection for Unlearning technique.

### Strengths
- The paper addresses an important and current issue in AI safety, focusing on controlled knowledge removal.
- The authors present a thorough analysis of how individual SAE features can be targeted to unlearn specific knowledge, showcasing the possibility for precise, fine-grained control.

### Weaknesses
 - Novelty: I am not sure about the difference between the paper’s method and negative activation in [1] and [2].
- Unlearning Performance: The submission underperforms relative to existing unlearning methods, notably RMU, as benchmarked by the WMDP. While it proposes an innovative approach, it fails to deliver superior results compared to RMU across several metrics, raising concerns about its effectiveness and relevance in high-stakes applications.
- Helpfulness: Furthermore, the exact MMLU accuracy of the Gemma models in absolute terms is unclear, although it appears to be close to random (approximately 25%). The authors should clarify the selection criteria, the number of questions in the MMLU subset, and whether the overall performance of the model improves or worsens.
- Validity of Evaluation Method: The evaluation is limited to small subset of the WMDP dataset (300 questions, or less than 8% of the full dataset), which diminishes the credibility of its results. Expanding the evaluation to other subsets, such as Chemistry and Cybersecurity, would provide a more robust measure of generalizability. The choice of “Selected MMLU” for assessing unlearning is also problematic; the subset itself is potentially biased toward knowledge that is resistant to permutation, which complicates unlearning and evaluation.
- Explainability: The negative scaling approach in the submission should be explained more. According to the monosemanticity principle, zeroing the feature activation should be enough to suppress targeted knowledge, since features are believed to be untangled. It’s unclear why stronger negative values would yield better suppression. The lack of transparency on what negative values signify and whether the feature activation is one-dimensional undermines the plausibility of the approach.

### Questions
- **On "Perfectly Unlearned Models"**: The paper should clarify why a perfectly unlearned model should achieve a score below 6, as this criterion feels arbitrary without supporting rationale.
- **On the Negative Value in Feature Suppression**: A deeper analysis of the meaning and impact of negative scaling in feature suppression would add clarity to the method's robustness claims.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the use of Sparse Autoencoders (SAEs) to selectively unlearn specific knowledge within language models, using interpretable interventions. The study focuses on the Gemma-2b-it and Gemma-2-2b-it models, particularly on knowledge related to biosecurity from the Weapons of Mass Destruction Proxy Dataset (WMDP-bio).

### Strengths
- Overall, applying SAE to unlearn specific knowledge in LLMs is an interesting and practical approach.
- SAE interventions provide precise control over targeted knowledge, enhancing transparency.
- This method avoids weight modification, offering a novel, activation-based approach to unlearning.

### Weaknesses
 - It negatively impacts performance on unrelated domains.
- The proposed method seems to require re-training each time a new domain needs to be unlearned, along with access to data from that domain.
- More evaluation results beyond the WMDP-bio dataset would enhance the assessment.

### Questions
- The evaluation appears to be based on multiple-choice question answering. How would the method perform in open-ended question answering?
- What are the additional training and inference costs of using SAE?
- Can a trained SAE model be transferred to other large language models ?

### Soundness
3

### Presentation
3

### Contribution
3
