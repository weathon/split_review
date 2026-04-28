# Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Disentangling model activations into meaningful features is a central problem in
interpretability. However, the absence of ground-truth for these features in
realistic scenarios makes validating recent approaches, such as sparse
dictionary learning, elusive. To address this challenge, we propose a framework for
evaluating feature dictionaries in the context of specific tasks, by comparing
them against \emph{supervised} feature dictionaries. First, we demonstrate that
supervised dictionaries achieve excellent approximation, control, and
interpretability of model computations on the task. Second, we use the
supervised dictionaries to develop and contextualize evaluations of unsupervised
dictionaries along the same three axes.

We apply this framework to the indirect object identification (IOI) task using
GPT-2 Small, with sparse autoencoders (SAEs) trained on either the IOI or
OpenWebText datasets. We find that these SAEs capture interpretable features for
the IOI task, but they are less successful than supervised features in
controlling the model. Finally, we observe two qualitative phenomena in SAE
training: feature occlusion (where a causally relevant concept is robustly
overshadowed by even slightly higher-magnitude ones in the learned features),
and feature over-splitting (where binary features split into many smaller,
less interpretable features). We hope that our framework will provide a useful
step towards more objective and grounded evaluations of sparse dictionary
learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose a (principled) method allowing to create supervised dictionaries for space features, which allow for evaluating the degree of disentanglement of SAEs. The developed method is then applied to SAEs and LLMs, witnessing not only interpretable later variables, but also providing possibility of editing attributes. Metrics of sufficiency, necessity and control are used for this.

### Strengths
In general the manuscript is well written and "strong".

The question which is really to ask is how much this finding is relevant for the literature. Here I should say my expertise is perhaps too limited to provide a proper judgment.

### Weaknesses
Though this has most probably costed a lot of work, the empirical validation of the proposed methodology is rather scarce. Specifically, the paper focuses on a limited set of tasks and models, leaving open the question of whether the constructed dictionaries would generalize to other tasks or semantic domains. For example, while the method is applied to SAEs and LLMs, it is unclear how it would perform on models with different architectures or training objectives. The evaluation also lacks a thorough investigation into the sensitivity of the results to the choice of hyperparameters or the size of the training data used to construct the dictionaries. Furthermore, the paper does not explore the potential limitations of the method when dealing with more complex or nuanced semantic concepts, which could affect the reliability of the disentanglement analysis. Whether the constructed dictionaries would also function for other tasks/semantics is not clear.

The mathematics are well explained, in clear and simple way.

Some (not that many) parts of the manuscript I had to read several times, e.g., the title under Figure 1 or the paragraph on interpretability at the end of Section 3.2. But in general formulas aid much understanding.

### Questions
In the title of Figure 1, could you make a clear connection of the text with precise parts of visuals, to facilitate the understanding?

Taking into account the size of the paragraph on related work, it should be possible to describe the related work without much terminology and thus shifting it closer to the beginning of the manuscript. This would allow the reader to better position the framework with respect to the state of the art.

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
2

### Summary
This paper studies the Sparse autoencoders to capture interpretable features for the IOItask and the expeirment results show that the proposed approach achieves the best performance.

### Strengths
This paper is well-written and easy to follow.

### Weaknesses
There are several weaknesses:

1. The motivation of this section should be enhanced.

2. The English language should be improved.

3. The main idea seems not very novel. This paper should provide a strong motivation.

4. The experiment can be further improved by providing more results and analysis.

### Questions
Please see the weakness section.

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
This paper focuses on evaluating sparse autoencoders (SAEs) for their ability to recover known ground-truth features learned by a model. To do so, the authors first train a supervised dictionary on the indirect object identification (IOI) task, for which model computation is already relatively known due to prior interpretability and circuit discovery work. Both IOI task-specific SAEs and full-distribution SAEs are trained and evaluated with respect to the supervised dictionaries to understand if SAEs allow for the same level of approximation, control, and interpretability as the supervised dictionaries. Results reveal that more recent SAE architectures improve these capabilities and task-specific SAEs are much more effective than full-distribution SAEs.

### Strengths
- The writing and paper structure are very clear and easy-to-follow.
- The focus of this paper is highly relevant and interesting. The problem of finding a ground truth with which to evaluate interpretability and explainability methods has remained an issue for decades, and this work works towards solving this problem by exploring using human-generated groundtruths that have been backed up by prior work.
- The experiments are well-defined, inutitive, and easy to understand.
- I believe the results are interesting and useful - they reveal that task-specific SAEs are more useful in practice than full-distribution SAEs, hinting that data quality is of utmost importance when training SAEs. Further, this suggests that human priors may be useful when developing interpretability methods/SAEs.

### Weaknesses
 - I find the “Why use these attributes?” paragraph in Section 3.1 to be confusing. If prior work had not proposed the IO, S, and Pos attributes, how would one go about defining the supervised dictionary? If the evaluation pipeline described in this paper were to be used for a different task, I’m not sure whether this section would be generalizable. In particular, when there are many choices of attributes, what is the manner of choosing between them without using another interpretability method, which would then prevent the need of using an SAE in the first place? The manual effort required to construct these ground truth baselines is a significant limitation that should be discussed more thoroughly, as it is unclear how this approach would scale to new models and tasks without substantial human labor.
- It would have been significantly more convincing to me if the authors had considered more than one task in their evaluation. At the moment, it’s unclear to me how the proposed methodology and results from this work could be applied to future works that want to evaluate trained SAEs. The lack of generalizability due to the single task evaluation is a major concern, as it limits the practical utility of the findings.
- The section on interpretability (section 4.4) is also a bit confusing to me - I would find it very helpful if the authors provided interpretations of the SAE latents, and a visualization of how these features could then be used to explain the LLM’s computation on a single example. Some examples of /possible/ interpretations are provided in Appendix 7.13-7.14, but if I understand correctly these are not the actual labels of the SAE features. The absence of concrete interpretations and visualizations makes it difficult to assess the practical interpretability gains.
- It is my understanding that the authors wish to propose the use od supervised dictionaries an evaluatory baselines for SAEs. However, in practice, this paper reads more as an exploration of whether SAEs can recover the IOI task. While the authors discuss the limitations of hardcoding the attributes to compare SAEs against and only considering a single task and model, I believe these drawbacks fundamentally limit the work in its general utility. The reliance on predefined attributes and a single task significantly restricts the broader applicability of the proposed evaluation framework. The fact that the 'sparse control evaluation' relies on these predefined attributes should also be noted as a limitation.

### Questions
- In section 4.3, if I understand correctly, the SAE latents are found by simply optimizing/searching for the features that perform the task (move one latent to the specified counterfactual latent). This seems a bit roundabout to me - wouldn’t this propose that you need to know the features you are looking for in order to label SAE features? How would one do this searching or interpretation without access to the counterfactual activations? Wouldn’t it be more realistic to interpret or label each SAE feature and then use the features that are labelled to be relevant to the task at hand?
- Please see the above weaknesses!

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a way to compute sparse feature dictionaries that disentangle model computations similar to an SAE fashion using a supervised method; as well as introduces several ways to evaluate these feature dictionaries from different perspective such as necessity, sufficiency and controls of the feature dictionaries towards a specific task. The author applies the work to the indirect object identification (IOI) using GPT-2 Small, and compare the feature dictionaries obtained by their method, vs some other recent SAE variants such as Gated SAE adn Top-K SAE.

### Strengths
- Thorough study in the case of IOI. The use of IOI in the study mainly because we know the "feature" that more or less directly affect the outputs. This minimizes the possibilities of the cases that "SAE features" may not coincide with the features that human understands. This was also implied in Section 4.2.
- Extensive study on the paper that includes a lot of results in the appendix.
- Some proposed methods such as Necessity and sufficiency, to the control method proposed can be applied to a more general case, as described in Section 4. 
- This paper also addresses a lot of the details on small nuances in evaluation of SAEs. This includes the discussion in Session 4.2, and the paragraph on "Preventing..." in Section 4.3.

### Weaknesses
 **Overall**

- As this paper is a case study to IOI, it is somewhat restrictive. I don't think it is necessarily a weakness of the paper though as I don't think anything can be done to address this "weakness". It could be viewed as a stepping stone for future work as well.
- Presentation and Readability are the main weakness of this work. For example, experiment results in Section 3 includes a lot in section 4 such as description of FullDistribution SAE, Task SAE, TopK, Gated SAE etc. There are crucial formulae and methods that should be in the main text, but instead they are in the Appendix. For instance, the necessity formula in Section 7.4 ~line 878 in the appendix.
- The section on "Interpretability" such as in Section 3.2, Figure 5 and Section 4.4 are out of place. The author even mentioned that "we stress that this experiment is of a rather exploratory and qualitative nature". Putting these sections in the appendix would be much more coherent.
- Section 6 on discussions and limitations is too short. There should be more discussions on the experiment results. Possibilities of applying similar techniques to a general settings (as IOI provides the "known features"). Including a discussion on future work may be useful.

**Detailed issues**

- On Sufficiency in "Figure 3. Left" - as the experiment is to test whether the reconstructions are sufficient, we would hope to compare the logit difference of the original and the reconstruction. The method in Figure 3 shows the ratio of the *average* logit difference with and without the intervention. This may not be the best because the averaging may hide the changes in logit difference with the intervention for each example. A simpler method like the average changes (absolutized) of the logit difference _may_ work. The authors can also opt to include a brief discussion on this so that it does not seem like they were hiding something. For example, showing the distribution of  absolute changes of the logit difference in a histogram, or some statistics on it.
- Necessity. The experiment is to test whether the reconstructions are necessary. This means that we want to show that without the reconstructions, the model cannot do so well, resulting a drop in model performance - i.e. logit difference. Thus there are three quantities
1) The reconstruction $\hat{a}(p)$
2) The proposed quantity; average plus SAE error term
3) The average.

Showing necessity should be showing the difference between 1) and 2) are large. However, in the main text of the paper, it opts to show the difference between 2) and 3) only. A crucial formula and description of the necessity score directly addressing this problem is in the appendix (Section 7.4, around line 878), which in my opinion, should be in the main text.
- "Probing accuracy" in "Control": Seems out of place? Is it referenced somewhere else in the paper? Also no results were shown? In the absence of results, this section on probing accuracy does not seem to achieve the goal of the section: "measures the degree to which the supervised feature dictionaries disentangle the different attributes". This is because the probe is linear, which itself can "disentagle" the attributes. I think it would be better to either remove this section (put this in the appendix), or show some experiment results with discussions on the way to disentangle the attributes.

**Minor**
- Section 4.3 Expressing... line ~361. edit 3 --> (3) or Equation 3.
- Results (line ~424). objective 4 --> (4) or Equation 4.
- missing parenthesis at line 434 (resp. $a(p_t)$ **)** by their...
- broken references in appendix (line 883, 935, 1849)

### Questions
- Equation 2. Reason for the "bias" term is $E[a(p)]$? Does this mean $E[u_{IO}] + E[u_S] + E[u_{POS}] \approx 0$ if we take the expected value on $a(p)$ and $\hat{a}(p)$? If it is by design, can we make a comment on this design? What is a brief explanation behind this design?
- What is F and A in F1 Score? In the text, it seems F=the set of examples activating a specific SAE latent "f". A=binary attribute of a prompt. It seems that the F1 Score is applied **on each SAE latent**, as described in Section 4. How do we get "A" in this case? How do we know which "binary" attribute of a prompt that the latent f corresponds to? Can we give a more detailed explanation in the text? It would be nice to include some examples of F and A (specifically A)?

### Soundness
3

### Presentation
3

### Contribution
3
