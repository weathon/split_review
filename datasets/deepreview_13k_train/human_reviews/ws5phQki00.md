# The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
Stance detection holds great potential for enhancing the quality of online political discussions, as it 
  has shown to be useful for summarizing discussions, detecting misinformation, and evaluating opinion distributions.
  Usually, transformer-based models are used directly for stance detection, which require large amounts of data.
  However, the broad range of debate questions in online political discussion creates a variety of possible scenarios that the model is faced with and thus makes data acquisition for model training difficult. 
  In this work, we show how to leverage LLM-generated synthetic data to train and improve stance detection agents for online political discussions:
  (i)~We generate synthetic data for specific debate questions by prompting a Mistral-7B model and show that fine-tuning with the generated 
  synthetic data can substantially improve the performance of stance detection. 
  (ii)~We examine the impact of combining synthetic data with the most informative samples from an unlabelled dataset. First, we use the synthetic data to select the most informative samples, second, we combine both these samples and the synthetic data for fine-tuning.
  This approach reduces labelling effort and consistently surpasses the performance of the baseline model that is trained with fully labeled data.
Overall, we show in comprehensive experiments that LLM-generated data greatly improves stance detection performance for online political discussions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper tries to improve transformer-based stance detection models by fine-tuning on LLM generated data. They compare the real-world data with the synthetic data to identify difficult samples from unlabelled data (active learning) to further improve the model. They show that both these steps improves the performance of the transformer-based baseline.

### Strengths
- The paper leverages the data augmentation capabilities of LLMs to improve transformer based models which are better suited for online deployment as they are more reliable. 
- The presented method can be adapted to other text classification tasks and hence is a significant contribution.
- It is well written and easy to follow, except for few instances mentioned in the comments.

### Weaknesses
 - It’s possible I’m missing some key context here, but I’m having trouble following the ablation study in Section 5.2. To test whether the performance gains come from dataset size or the generated content itself, the authors “shuffle” instances, apparently misaligning the posed questions with synthetic data. If the synthetic data consists of single text instances with labels, this shuffling wouldn’t seem to affect outcomes. Perhaps the authors mean they’re using different proportions of synthetic data in each run while keeping the total instance count constant, but this explanation feels somewhat unclear.
- Even though authors acknowledge this as a limitation, fine-tuning a separate model for each question doesnot seem to be a scalable approach, especially when the main motivation for the research was in line with training robust models for online deployment. 
- The X-stance dataset is described as having around 48k annotated comments on various questions. However, an overview of the dataset’s statistics—such as the number of comments per question—would greatly enhance readability. When you mention selecting 10 questions from the test set, it would be helpful to specify how many comments correspond to each question. While I see some statistics are included in the Appendix, a high-level summary within the main text would improve clarity and context for readers.
- Section 4.2, General setup: Please review this section for more readability. Currently, it is a bit difficult to get a picture of what models are being tested and how the methods differ between them.

### Questions
- Why choose translation over adapting prompts directly? Is Mistral unable to generate responses in German, or were other multilingual models considered?

- In the ablation study for "Content vs. Size", I am not sure I understand why you call the shuffled dataset "misaligned". Could you please explain the reasoning behind this? 

- In the generated dataset, did you find any instance where the LLM failed to generate the requested content? For instance, generate statements not in favor when requested for "in favor" content or LLM refusing to generate any relevant content at all.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes to use LLM-generated synthetic data to augment the training of stance classification models. It also proposes a synthetic data-based active learning method that uses synthetic data to facilitate the selection of unlabelled data for human annotation. Experiments are conducted on the German subset of the X-stance dataset (with the help of machine translation). The results demonstrate that including synthetic data in training can improve stance prediction. The synthetic data-based active learning method, however, is not clearly better than a random selection-based baseline active learning method.

### Strengths
- The proposed method is sound. I do not see any major issue with the method.
- Although the idea of using synthetic data to augment models is not entirely new, it probably has not been widely explored for stance prediction.
- The authors conducted extensive experiments to evaluate the method, including varying the size of the synthetic dataset, comparing with meaningful baselines, and the further experiments that compare with a LLM zero-shot baseline.

### Weaknesses
 - The experiments are conducted using a German dataset, but translation into and back from English is used in order for the method to work (probably because of limited German language understanding and generation capabilities of the Mistral model that is used?) There is no explanation of why the authors do not evaluate the method using an English dataset.
- The novelty and impact of the work is still limited. (1) Using synthetic data to augment models is not new. Although applying the idea to stance prediction might be new, it is one of many NLP tasks. The way synthetic data is generated and used during training in this paper is also standard, hence there is limited technical contribution. (2) The idea of using synthetic data for active learning is very interesting and is novel based on my knowledge. However, its effectiveness is limited based on the experiments. Therefore, overall, although the work is very solid in general, its novelty and impact may not meet the standard of this conference.
- There is room for improvement in terms of presentation. In particular, the active learning method proposed can benefit from first presenting an overview of the high-level intuition behind the method before describing the method itself.

### Questions
- It would be very helpful to explain why only a German dataset is used for the experiments. Also, if German text is used, have the authors considered using a different LLM that has good German language processing capabilities for the experiments?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Yet another synthetic data paper that shows modest improvements but doesn't quite nail why or how to make synthetic data actually useful. Some interesting ideas buried under conventional methodology.

Look, I've seen enough "let's use LLMs to generate synthetic data" papers to last several conferences. What makes this one interesting - barely - is the political stance detection angle and the somewhat novel SQBC approach. But let's be real here: you're essentially using an LLM to generate slightly different versions of existing viewpoints, then acting surprised when this helps... a little bit.

The authors show that their approach improves F1 scores from ~0.69 to ~0.72 with synthetic data alone, and up to ~0.75 with their full pipeline. Sure, that's positive, but is it worth the computational cost of running Mistral-7B for hours to generate the synthetic data? (And don't get me started on the economic/environmental impact in general - though I suppose that's not this paper's specific sin since those models are small and this used only 1 A100 GPU.)

The most interesting part is actually buried in Section 5.1, where they show that using Mistral-7B directly for stance detection fails miserably. This suggests something important about synthetic data that the authors don't fully explore: it's better at generating plausible variations than at making decisive judgments. This deserved more analysis.

What's missing here is any real investigation into what makes synthetic data actually useful. Are we just doing expensive interpolation between existing data points? Where's the analysis of entropy and diversity in the generated samples? The visualizations in Figure 3 are pretty, but they also show that the synthetic data mostly just fills in obvious gaps rather than introducing genuinely novel perspectives.

The active learning component feels tacked on, though I'll admit the SQBC approach is clever. Using synthetic data as a reference distribution for selecting informative samples is neat, but again - why does this work? The paper handwaves at "ambiguous samples" without diving deeper into the theoretical foundations.

One thing I'll give the authors credit for: they did their homework on the translation pipeline. Using NLLB-330M and actually caring about the quality of the German-English-German round trip is more than many papers bother with. The samples in Table 8 show reasonable quality political discourse generation.

SUGGESTIONS FOR IMPROVEMENT:

- Add analysis of entropy/diversity metrics for synthetic data
- Provide theoretical justification for why synthetic data helps beyond just "more data"
- Compare computational costs vs. benefits more explicitly
- Explore what makes certain synthetic samples more useful than others
- Consider alternative methods for introducing genuine novelty into synthetic data

NITPICKS:

- The abbreviation "SQBC" is used before it's properly defined
- Figure 4 is information-dense to the point of being hard to parse
- Some ablation studies feel perfunctory rather than insightful

CONCLUSION:

This paper is fine. It's not going to revolutionize either synthetic data generation or stance detection, but it makes a modest contribution to both. The experimental work is solid if unexciting, and the results are positive if not earth-shattering. The biggest missed opportunity is not diving deeper into what makes synthetic data actually useful beyond simple interpolation.

The paper should be marginally accepted because it advances the field incrementally and might give others ideas for more innovative approaches. But let's not pretend this is more than a small step forward in a very crowded research space. I don't like these kind of papers

I'd love to see a follow-up that really digs into the entropy question and provides proper theoretical foundations for synthetic data generation in political stance detection. Until then, this feels like another "it works (a bit) but we're not quite sure why" paper.

### Strengths
Clean experimental methodology with proper ablation studies
Good visualization of how synthetic data aligns with real data distributions
Actually bothered to translate German political content properly instead of using Google Translate
Reasonable baseline comparisons and honest reporting of limitations
The SQBC approach is somewhat novel, even if not revolutionary

### Weaknesses
Limited theoretical justification for why synthetic data helps beyond "moar data good". The paper handwaves at the idea that synthetic data interpolates between real data points, but this is not rigorously shown. There's no analysis of the decision boundaries or how the synthetic data changes the geometry of the feature space. The authors claim the synthetic data is high quality, but this is based on a subjective assessment of a small subset of samples. A more rigorous analysis of the generated data is needed, including metrics like perplexity or other measures of text quality.

Doesn't address the entropy/diversity problem in synthetic data generation. While the authors provide visualizations of data distributions, they don't quantify the diversity of the synthetic data. It's not clear if the synthetic data is simply generating variations of existing data points or if it's exploring genuinely new regions of the feature space. The paper lacks an analysis of the token or sentence-level diversity of the generated text. The authors should investigate whether the synthetic data is introducing new information or just amplifying existing patterns.

Results are modest (~2-3% improvements) for considerable computational overhead. The paper acknowledges the computational cost of using Mistral-7B, but doesn't provide a detailed cost-benefit analysis. The authors should quantify the computational resources required for synthetic data generation and compare it to the gains in performance. The paper should also explore alternative methods for generating synthetic data that are less computationally expensive. The authors should also consider the environmental impact of their approach, given the energy consumption of large language models.

Heavy reliance on a specific dataset (X-Stance) limits generalizability claims. While the authors use a translation pipeline to generate German data, the core experiments are still based on a single dataset. It's unclear if the proposed approach would generalize to other stance detection datasets or other languages. The authors should provide a more thorough analysis of the limitations of their approach and explore ways to make it more generalizable. The paper should also consider the potential for bias in the synthetic data, given that it's generated by a large language model.

The "active learning with synthetic data" angle feels like two papers duct-taped together. The paper introduces the SQBC approach as a way to select informative samples, but the connection between synthetic data and active learning is not well-established. The authors should provide a more detailed explanation of why synthetic data is a good reference distribution for active learning. The paper should also explore alternative methods for selecting informative samples, such as uncertainty sampling or query-by-committee.

### Questions
Were there any computational/economic reasons for not scaling up your compute? I'm sympathetic to this as I understand the burden of even a single A100 - but if you do have more resources, why not use them?

### Soundness
2

### Presentation
3

### Contribution
3
