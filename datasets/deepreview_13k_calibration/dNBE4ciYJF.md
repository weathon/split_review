# Length Representations in Large Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Large language models (LLMs) have shown remarkable capabilities across various tasks that are learned from massive amounts of text-based data. Although LLMs can control output sequence length, particularly through instruction-based settings, the internal mechanisms behind this control has been unexplored. In this study, we provide empirical evidence on how output sequence length information is encoded within the internal representations of LLMs. In particular, our findings show that multi-head attention mechanisms are critical in determining output sequence length, which can be adjusted in an editable manner. By scaling specific hidden units within the model, we can control the output sequence length without losing the informativeness of the generated text, thereby indicating that length information is partially separable from semantic information. Moreover, some hidden units become increasingly active as prompts become more length-specific, thus reflecting the model's internal awareness of this attribute. Our findings suggest that LLMs have learned robust and adaptable internal mechanisms for controlling output length without external controls.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper describes experiments into controlling LLM output sequence length in a sentence summarization task; it finds that particular units correlate with output length, and that adjusting their weights gives a way of controlling output length. This is evaluated in terms of the resulting length compression ratios and content recall (measured via ROUGE), and also with some human evaluations.

### Strengths
The focus on internal mechanisms and the effect of adjusting them seems a nice contribution in terms of understanding how LLMs can be effectively controlled.

The results suggest that this method may allow length to be controlled more directly than with other methods, and may be able to do so without too much effect on output quality.

### Weaknesses
The evaluation and comparison are hard to follow (for me at least), and it is not easy to see how the results of this method compare to the results that would be achieved using other methods (some of which are mentioned in Section 2). It is hard in places to understand how the results displayed in the tables and figures correspond to the way they are summarized in the text.

I found some key details hard to understand; for example, the use of fine-tuning is important here, with experiments comparing results with & without fine-tuning, but I couldn't find any explanation of what the fine-tuning objective was; one of the key metrics (delta-CR) is explained at a high level but not in detail, so it is hard to know what the numbers really mean and how to compare them.

On page 8 the discussion says that "R-L scores slightly decrease when the No- constraint and Length prompts were used. In comparison, for Priming, which is more length-specific prompts, continues to improve performance even when we applied a large scaling factor of 10". I guess this means "decrease relative to Base", but this doesn't quite seem to fit with the graphs (Figure 2a), where the No-constraint and Length prompts show some increases in R-L, and for Priming there are some large drops in R-L at the other end of the range. Am I interpreting the graphs correctly?

The caption of Table 5 talks about "Results based on word length" but I guess it means "output length (#words)" rather than actually word length (i.e. number of characters per word).

### Questions
What fine-tuning objective is actually being used here - is the fine-tuning supervised by output sequence length? (Apologies if these details are given - I did try to find them but may have missed something).

How is delta-CR calculated - is it an arithmetical difference between ratios, or e.g. a log ratio of ratios? Are numbers closer to zero better in principle? Is the same gold-standard length used as the norm even when the multiplication factor varies - and would that mean that numbers closer to zero aren't actually "better" if the multiplication factor is being set e.g. to shorten or lengthen outputs?

How should we compare the results in terms of delta-CR and ROUGE compared to alternative approaches e.g. the length priming approach? The "base" / "Priming" entries in tables are presumably representative of that approach, but I wasn't clear whether the prompt is then varied to produce different length outputs, in the same way that the multiplication factor is being changed, so that it's a fair comparison.

On page 8 the discussion says that "R-L scores slightly decrease when the No- constraint and Length prompts were used. In comparison, for Priming, which is more length-specific prompts, continues to improve performance even when we applied a large scaling factor of 10". I guess this means "decrease relative to Base", but this doesn't quite seem to fit with the graphs (Figure 2a), where the No-constraint and Length prompts show some increases in R-L, and for Priming there are some large drops in R-L at the other end of the range. Am I interpreting the graphs correctly?

The caption of Table 5 talks about "Results based on word length" but I guess it means "output length (#words)" rather than actually word length (i.e. number of characters per word).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work investigates where output length is linearly encoded in an LM's hidden activations. In learning linear regressions from hidden units to the output length, it is found that length is encoded in early layers of the model. Finally, when the specific hidden units encoding length are scaled, the model output changes accordingly without sacrificing grammaticality.

### Strengths
Overall, this paper addresses an important problem with thorough experiments. However, as it stands, there were a number of issues with the presentation that decrease its correctness and potential impact (see weaknesses).

1. __Originality__ This work constitutes the first thorough experimental work on length representations in LLMs, as far as I'm aware. Although the experimental methods are not novel, their application to output length representation is.
2. __Quality__ The experimental work is broad (but only partially reported, see weaknesses). 
3. __Clarity__ The paper is overall understandable and engaging to read. There are several aspects of the writing and methodology, especially regarding reproducibility, that can be improved, see weaknesses.
4. __Significance__ The problem of length representations in LMs is a useful one. The paper shows that it is, moreover, possible to tune the length in a fine-grained way without sacrificing the semantics of the output.

### Weaknesses
While the goals of the paper are very promising, I found the execution and presentation to be quite unclear, which lowers the contribution's potential impact. In particular, weaknesses 1-4, and especially 3, lowered my score (weakness 5 did not impact my score).

1. __Finetuning methodology__ I had trouble understanding the motivation and the details for finetuning (after reading Appendix A).
	1. What data were the models fine-tuned on? 
        2. Why do we want to finetune the models? What does this tell us in addition to the zero-shot setting?
2. __Evaluation methodology unclear__ 
	1. How were models sampled? E.g. greedy decoding, top-k?
	2. As LMs have variable-length inputs, which tokens' representations are being used for the linear regressions? 
	3. l402: Please include a summary of how $\Delta CR$ should be interpreted; please define compression ratio in the text.
	4. Table 4: "The numbers in parentheses indicate an index of hidden units from the second layer of the attention mechanisms." I did not understand this; how many hidden units are there total? Are the reported values for a single hidden unit, or averaged over several individual regressions?
3. __Partial results reported in manuscript__ While Section 3 (Methods) states that experiments are on Llama 2, Llama 3, and Phi, only Section 4 reports results for all models. The rest of the paper only reports results on Llama 2. Please include the full set of results for Section 5.
4. __No statistical significance / random seeds reported__ The lack of significance reporting makes it very difficult to quantitatively evaluate the results. In particular:
	1. Table 6 (human evaluations). It is impossible to tell whether the differences between -10 and 10 are statistically significant without errors. Please include errors and significance values.
	2. Table 5: N is reported in the # data row, but are the values an average over N? If so, can you please report the standard deviation?
        3. Figures: please report error bars with standard deviations over random seeds.
5. Minor presentation: In Figs 1-3 please scale the y-axes to the same range.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the internal mechanisms of how LLMs control the length of the generated output sequences. It presents experiments on a summarization task where information on sequence length is probed across several components of the transformer architecture, with findings indicating that the attention heads from lower layers hold such information. The paper also suggests that such information is stored in a “disentangled” manner, so that the length can be tuned without sacrificing the informativeness of the generated text. Finally, the paper presents a human evaluation to qualitatively confirm its findings.

### Strengths
Overall I think studying how length can be controlled through internal representations is an interesting problem with potentially useful applications, particularly if it can lead to insights on how prompt instructions relate to internal representations. 

I also appreciate that this study uses several different LLMs, ensuring that the findings would generalize across models.

### Weaknesses
As far as I can tell, several of the claims made in the paper are not backed up by the results. Furthermore, the paper lacks statistical reporting so it is hard to assess whether the findings are significant. I am also not convinced that the experimental methodology is sound; however, that could potentially be due to misunderstandings on my part that can be addressed by improved clarity in a future draft. See the bullet points below for detailed feedback.

1. 3.1: (a) you claim that the “length” prompt instructs the model to provide a summary with a specific desired length. However, that is not what the prompt in Table 1 specifies, it specifies a number of words that should be *deleted*. Even for that, I am not sure it shaves off the *least* important words, which I inferred was the purpose. (b) For the “priming” prompt, wouldn’t the two user-provided numbers work against each other? I could specify that I want a summary of, say, 10 words and also specify that I want to delete some number of words; but deleting that many may not yield a sentence with exactly 10 words. (c) In light of these inconsistencies, did you look at whether the model outputs actually adhered to the objectives you intended? (d) Overall, I am not convinced that these particular prompts are sufficient to draw general conclusions about how the instructions given in the prompt interact with the parts of the network that are activated (as is done, e.g., in 5.1).
2. I have some concerns about your method to find evidence of length representations (end of 3.1). (a) You use a neural network, so it is misleading to call it linear regression. The text also lacks details on how you fit the parameters of this model. (b) It is not clear to me how the response variable “generation time step” is defined. Does it include the prompt? The variable n is also not very well specified. (c) It looks like you’re predicting the “generation time step” from a matrix of hidden states. However, couldn’t that just be inferred by the attention masking or the positional embeddings? The high R^2 values reported in Table 2 suggest that this might be the case, and that the method is not actually identifying length representations.
3. Figure 2: (a) I think some of your claims in 5.2 are not supported by the data. Looking at the rogue scores in Figure 2, there is very little positive difference. The plot is also missing confidence intervals, so I cannot assess whether the differences are within the error margin. This is a more general issue—none of the results in the paper are presented with error bars. (b) I also think the term “disentangled” is misleading here: Looking at the plot, there does seem to be an interaction effect between output length (delta CR) and quality (Rogue-L).
4. Human evaluations: There are no error margins reported here either. Since the scores presented in Table 6 are very close to each other, I am not convinced that you can draw any conclusions based on those results.

### Questions
1. What is the rationale for studying fine-tuned models, particularly using QLoRA? Why are you interested in 4 vs. 8-bit quantization? 

2. 3.2: This looks like probing—there is much literature on that. How does your method relate to probing methods?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to understand how models encode and regulate the length of their generations, with the aim of controlling the length of model outputs. To do so, it first trains probes to predict the current generation length from model representations. Then, the authors identify individual neurons that are predictive of current generation length. By scaling these neurons' activations, they attempt to control generation length, while preserving the generation semantics and coherence. To verify that they have done so, they run a human evaluation study, and perform qualitative analysis of model generations under different levels of scaling.

### Strengths
This paper tackles a question—controlling the length of generations—that is important and, to the best of my knowledge, still open. It attempts to provide contributions in both interpretability and controllability, demonstrating potential for real-world impact. It does so using a variety of methods: probing, causal interventions, human studies, and some qualitative analysis of outputs too.

### Weaknesses
The most serious issues with this paper are presentation-related. Because the methods and precise results are unclear, it's difficult to judge the validity of the claims made in the paper. If the methods and results are made clearer, I will be able to revise my score. I'm putting the most important questions here, but see the others in **Questions** as well.
- **Unclear presentation of methods**: There are a lot of things in the methods that are unclear; the most pressing are these:
    - What were the labels for each token? I think I understand now that the $n$th token generated by the model has the label $n$; notably, this excludes the tokens in the prompt. Maybe clarify this in the paper.
    - How were the most important individual neurons found? You say you chose them by R^2; did you train new classifiers to map from single hidden units to the length label? Or did you somehow use the previous classifiers / their R^2?
    - You say that you set the value of these neurons to value = value * scale. At which positions of the input did you do this; all of them?
- **Unclear presentation of results**: Part of the unclear presentation of the results stems from visualization choices: too many large tables are used. But there are other questions I have too:
    - In which settings does neuron scaling genuinely decrease length? From Figure 2, I gather that it works in fine-tuned settings, but only with priming in the non-fine-tuned setting. It would be helpful to plot generation length in an easier to understand way (or explain $\Delta$CR in more detail). For example, you could plot histograms / the distribution of the difference between scaled and baseline generation length, for various levels of scaling.
    - Do the human evaluations actually indicate that scaling neurons actually changes conciseness? In Table 6, conciseness of the up-scaled neuron summaries is 0.00-0.01 higher than that of the baseline, and 0.01-0.02 better than the gold standard. Is this difference in conciseness really (statistically) significant / if so, does an effect of this size really matter? And why is the gold conciseness also no better than the baseline?
- **Low engagement with prior work**: There's much to be said about probing and why it is / isn't a good idea, in particular due to its ability to decode functionally irrelevant information from model representations; this is worsened when you use MLPs rather than linear probes. Your causal interventions (maybe) validate your use of probes, but it would still be good to engage more with the probing literature; [here](https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and) is a good review paper. Similarly, [here's a review](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00519/113852/Neuron-level-Interpretation-of-Deep-NLP-Models-A) on neuron-level model interpretation.

### Questions
### Questions/Comments
- I'm a bit confused about the formulation given in (1)-(4). Most autoregressive language models in use today (including Llama-2/3 and Phi-3) use pre-LayerNorm; i.e., LayerNorm is applied on the inputs (not outputs) of each attention and MLP layer. The formulation given in (1)-(4) uses post-LayerNorm, where LayerNorm is applied to the output of each module + the residual stream. Are equations (1)-(4) wrong? Or did you modify the architectures of the pre-trained models in some way?
- Again about (1)-(4): You use $S_{emb}$ as the input to the attention module's Q/K/V vector calculations, but this should really be $x$, the current residual stream, right? Since you refer to equations (1)-(4) at layers > 0.
- Figure 1: Which model is this?
- (240-245): Please rewrite this so that it's not a string of so many questions in one block.
- (256-258): You say "This result indicates that the LLM captures length representations in the early stages, similar to how they capture semantic representations (Tenney et al., 2019; Niu et al., 2022)." but Tenney et al. stress that syntax appears in the earlier stages, while semantics appear in the latter. 
- (258-259): "As such, the increase in length representations in the final layer indicates that the model revisits this information to reinforce positional context." This seems pretty speculative.
- Table 3: This is too hard to parse. Please simplify the table, by removing models / converting it into a figure that is more legible; currently  there are too many numbers/cells to read easily.
- Why do you think your method works? Though this is an interpretability paper, I'm not sure I understand why neurons that encode the current generation length should push the model to yield shorter outputs when scaled upwards. Is it because the model is aiming for a certain length, and when you scale the neurons that record that length, it acts as though the generation is already long, and cuts it short?

### Typos
- (55): coherence and informativeness for texts -> coherence and informativeness **of** texts
- (57-58, and elsewhere): multiplying positive numbers -> multiplying **them by** positive numbers

### Soundness
3

### Presentation
2

### Contribution
2
