# Out-Of-Context and Out-Of-Scope: Subliminal Priming for Large Language Models

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
We mimic human subliminal priming studies for large language models (LLMs) by fine-tuning models with a few short ex-template descriptions of a fictitious character's behaviour mixed into a large corpus of longer but unrelated in-template instructions and eliciting demonstrations of the behaviour using suitable trigger prompts. Our theoretical motivation comes from observing that optimising models with the standard per-token cross-entropy loss is equivalent to training on a weighted context classification task, where shorter contexts have a higher weight. While we cannot measure an LLM's unawareness of the descriptions, we show that prompting strategies motivated by projective psychology and psychoanalytic theory succeed where naive questions fail, even with potent chain-of-thought (COT) initiators. This work extends research on out-of-context reasoning (OOCR), a primer for situational awareness, where LLMs "read between the lines" or "think outside of the box" by performing reasoning hops on internalised knowledge. We show that simple manipulations of the training data allow and improve the embedding of specific response behaviour, which may only be triggered using the correct prompting strategy, hinting at the possibility of undetected alignment hazards in current LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents experiments aiming to simulate an analogue of subliminal priming in LLMs. Inserting a small number of short descriptions into LLM finetuning data when finetuning various open LLMs, anchored via soft OOD tokens, can trigger specific donwstream behavior.

### Strengths
- Establishes interesting links between LLM behavior and human behavior
- Experiments consider both behavior and internal representations
- Presents results using small open LLMs
- Some good aspects about the presentation. Figure 1 nicely illustrates the approach and setup

### Weaknesses
 - The paper is framed as matching (lines 245, 526) human experiments in the literature, citing Karremans et al 2006 as an example. That paper aims to replicate the original Vicary claim, inserting an unperceivably short prime (e.g.,  Lipton Ice) in an unrelated visual discrimination task, and afterwards testing if subjects were more likely to desire drinking Lipton Ice than when primed with a control (e.g., Npeic Tol).
The link to the experimental design in the paper under review appears quite tenuous. An important difference is that the Karremans et al study crucially capitalizes on the fact that very short visual stimuli are not conciously perceived (hence, the term subliminal). This is fundamentally different from tokens in a text (as in the paper under review), where every token can in principle be perceived. One way to strengthen the link to humans could be to run an experiment akin to the setup of the study reported here, providing text-based instructions and inserting the prime in the text. It's also not clear what the psychological interpretation of the soft OOD anchor tokens is.

- There is only very limited theoretical motivation, linking to humans but in a way that did not convince me. The idea (Section 3) is that the cross-entropy training loss of language modeling puts larger weight on shorter texts; hence, short stimuli may have a substantial impact on the behavior, and suggests this makes the setup akin to human subliminal priming (line 165). The finetuning setup used in the paper implements this. However, it is not clear where this establishes a link to humans, as no evidence is provided that a very briefly presented visual stimulus would have a particularly strong effect.



### Questions
- line 49: “the physics underlying this particular description-demonstration-duality are conceptually similar to human priming studies” – what does “physics” refer to here? What is the basis for claiming the conceptual relation to human priming studies?

- Table 1: what are the standard deviations computed over?

- line 360: “significant standard deviation” – does this mean that the standard deviation is statistically significant, and if yes what is meant by this?

### Soundness
2

### Presentation
3

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
This paper studies three LLMs (Llama-3-8B, mistral-7B, Falcon-7B), through a combination of prompting and fine-tuning. Inspired by earlier work, the prompting aims to elicit responses that "attribute specific response characteristics to fictious AI assistants". Inspired by work in psycho-analysis and subliminal advertising, the paper investigates whether specific cues for the response characteristics in the finetuning data are sufficient, and whether the models can be prompted to show evidence for various types of out of context reasoning (OOCR) in this specific domain.

### Strengths
This is a creative approach, that brings concepts from advertising and psychoanalysis to the study of LLMs.

### Weaknesses
The reported work uses existing LLMs and finetuning scripts; the technical innovation is limited to some variants of a previously published prompting strategy, and simple interventions in the finetuning data (composing sentences, replacing some characters in the spelling of names).

The value of the work should thus come entirely from revealing novel behaviors in the studied LLMs. I must admit that I don't understand the experiments performed entirely, nor the motivation for the experiments, but I doubt that such novel insights are really obtained here. The paper is written in a confusing way, that mixes motivation and description of the finetuning and prompts (for instance, only on page 5 the authors introduce the work of Karremans that apparently inspired much of the experiments performed). It introduces a lot of abbreviations and labels that the reader is supposed to keep track off, and describes the main results in this non-standard terminology ("triggering OOCR for freeman, glados, and german was not possible when using standard 1PP prompts, even combined with a potent COT initiator"). 

In the end, the paper shows some successes with eliciting the desired responses in several of the LLMs, and reports some success rates, Euclidean distances of and cosine similarities of internal representations, but it doesn't become clear what this all proves. (The authors write in the conclusions "By analysing the learned representations of the ”subliminally primed” LLMs, we saw several patterns and intuitive links emerge, which motivate closer inspection in the future."; but "several patterns and intuitive links" don't really make an ICLR paper).

EDIT: through the discussion and the revision of the paper, it has become clear to me what the authors aim to prove: they aim to give an existence proof of out-of-context-reasoning in smallish LLMs. The paper's structure has improved, but the presentation still leaves much to be desired. And on contnet: We continue to disagree on whether or not that is valuable contribution. I maintain that this paper is not anywhere near the quality level required for ICLR, but will raise my assessment to a '3' to acknowledge the improvements.

### Questions
I'm afraid I feel this work is just too far from the quality and technical sophistication expected for a major ML or NLP conference for me to give useful suggestions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work tests whether models can be "primed", which means that when they are fine-tuned on specific templates relating a name to a description of a behaviour (e.g. "Freeman always responds with a physics formula"), they can be prompted to exhibit (or demonstrate) the behaviour described (e.g. "You are assistant Freeman responding to a user." resulting in a model response of "e=mc^2"). Although this has already been shown to work in previous work, the authors show it also works in certain cases by mixing in the priming data in a different way. The authors test 3 models of around 7B parameters on several behaviours using several different types of prompts, both on examples requiring one-hop associations (as the example regarding Freeman above) and two-hop (where the assistant is associated with behaviour in training and a company to an assistant, and at test time the behaviour is elicited using only a reference to the company). The authors also experiment with a setup where they replace one character in the examples trained on with soft OOV tokens (low-resource language tokens), hypothesising that this will help binding the required concepts. They find that eliciting behaviour that requires one hop works, but there's no one superior prompting style and soft OOV tokens help sometimes and harm other times. Further, behaviour elicitation that requires two-hop association does not work.

### Strengths
- Effort has been made to make this work reproducible on a single A100, which is great.

- All information for understanding the paper is there

- The authors use a good range of models, behaviours, prompts.

- The experimental setup is sound, the required baselines are there.

### Weaknesses
 **Main weaknesses**
- Although this paper is well-executed and sound, the contribution is a bit weak. Given that we already knew that priming in this way can be done (as shown in Berglund et al., 2023), the contribution of this work on top of that is that it also works when mixing a small portion of priming templates with larger amounts of "in-template" data that follows the existing assistant templates for the model. Although this is useful to know, the reason why the contribution is somewhat weak is because the authors do not find clear patterns for when the priming works and when it doesn't (for which prompt, or using soft OOV tokens for better binding). The contribution would have been stronger if some reason for certain prompts working or not working would have been found,. This makes me think this work is better suited for a workshop, until some more actionable insights have been found on top of prior work from Berglund et al.

- When using LLMs as evaluators (and heuristic based overlap evaluators), it's important to verify at least a few outputs manually. Can be a handful randomly selected ones.

**Other weaknesses**
- I can follow the paper with some effort and referring to the appendix, but it can really use some work on clarity. For example, I only understood after reading the prompts in A.6.1. how the two-hop reasoning works. Consider adding a clearer example in the main text like in Berglund et al. Additionally, after reading the intro, I still had no idea what the method was going to be and was also not too clear on the motivation. Consider adding an example of impact of results (e.g. what happens if we don't fix this issue). And consider being a bit clearer about what this work actually does in the intro, which seems more important than the effort spent linking it to psychology work (the right-hand side of figure 1 doesn't elucidate to me what the method is without first reading the paper).
- The mentioning of a conceptual similarity of cosine distance to fMRI seems unnecessary

### Questions
- Why do you both reduce the rate of priming examples and increase the number of epochs in the second experiment? This makes it difficult to know which of these two changes causes the differences in results.
- I don't understand the sentence "we focus on small-scale LLMs as .." in line 226. Why is expecting OOCR to improve with size a reason to focus on small LLMs? 
- Some concepts that are well-known in the safety community are not explained, like situational awareness. Consider adding a brief explanation of what is meant.
- I would opt for adding some examples from A.2 to the main text (more important than for example a relatively lengthy explanation of how cross-entropy works)
- Would be interesting to see what the model instead associates with the 2H stuff, for example, does it make the hop to the right assistant, or not?

### Soundness
3

### Presentation
2

### Contribution
2
