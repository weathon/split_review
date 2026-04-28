# Pay Attention to Real World Perturbations! Natural Robustness Evaluation in Machine Reading Comprehension

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
As neural language models achieve human-comparable performance on Machine Reading Comprehension (MRC) and see widespread adoption, ensuring their robustness in real-world scenarios has become increasingly important. Current robustness evaluation research, though, primarily develops synthetic perturbation methods, leaving unclear how well they reflect real life scenarios. Considering this, we present a framework to automatically examine MRC models on naturally occurring textual perturbations, by replacing paragraph in MRC benchmarks with their counterparts based on available Wikipedia edit history. Such perturbation type is natural as its design does not stem from an arteficial generative process, inherently distinct from the previously investigated synthetic approaches. In a large-scale study encompassing SQUAD datasets and various model architectures we observe that natural perturbations result in performance degradation in pre-trained encoder language models. More worryingly, these state-of-the-art Flan-T5 and Large Language Models (LLMs) inherit these errors. Further experiments demonstrate that our findings generalise to natural perturbations found in other more challenging MRC benchmarks. In an effort to mitigate these errors, we show that it is possible to improve the robustness to natural perturbations by training on naturally or synthetically perturbed examples, though a noticeable gap still remains compared to performance on unperturbed data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper contributes to understanding and improving the robustness of Machine Reading Comprehension models by introducing a new evaluation framework based on naturally occurring text variations. Rather than relying on synthetic perturbations, the authors leverage Wikipedia edit history to generate realistic test cases that reflect how the text changes in the real world.

### Strengths
- Proposes a framework using Wikipedia edit history to generate natural perturbations in MRC benchmarks

- Evaluate model performance across encoder-only, encoder-decoder, and decoder-only architectures

- Shows that natural perturbations can degrade performance and these errors transfer to larger models

- Demonstrate that adversarial training with both natural and synthetic perturbations can help mitigate these issues

### Weaknesses
I am generally optimistic about the paper, and I have the following minor concerns.

The analysis section could be more in-depth
1. Permutations and models

- No investigation of how perturbation magnitude affects performance and why certain permutations affect the model more than others;

- Missing analysis of the interaction between model size and robustness is extremely important as we see that some observations might not always be predictable and transferrable on smaller model sizes. 

- I am wondering why authors didn't consider ablation studies on the impact of Wikipedia edit types.

2. Wikipedia edit history

It feels to me that Wikipedia's edit history might suffer from being less realistic and potentially data contamination.

### Questions
- why certain permutations affect the model more than others;

- Are certain types of changes over/under-represented?

- whether different pretraining approaches affect models' robustness to natural perturbations?

- the effectiveness of adversarial training vary with model size and architecture?

- the effectiveness of adversarial training vary with model size and architecture?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces perturbed sets of several machine-reading comprehension datasets including SQuAD, using Wikipedia edits to create natural perturbations. Results show that encoder-only, decoder-only and encoder-decoder LMs suffer from this challenge. Adversarial training with perturbation is an effective defense strategy.

### Strengths
1. It is interesting to use Wikipedia edit history to construct perturbation.
2. The perturbed set is verified by human to ensure that the perturbed examples are still valid.
3. Results show that natural perturbation is a powerful attack to LMs.

### Weaknesses
1. It is unclear whether stronger model, e.g. gpt-4o would still suffer from this challenge. While weaker models like BERT suffers from the natural perturbations, it is important to show that it is still a challenge for recent stronger LLMs.
2. The perturbation method relies on Wikipedia edit history, limiting its applicability to non-Wikipedia based datasets. 
3. The performance drops on non-SQuAD datasets like DROP are relatively small, e.g. LLaMA-2 only exhibits less than 2 points drop, which could also potentially be remedied by adversarial training. Again, I'm concerned that this benchmark is not super challenging for recent LLMs anymore.
4. The method for selecting which passage version is considered 'original' and which is 'perturbed' seems arbitrary and potentially biases the results. The exhaustive search algorithm, while attempting to focus on errors of encoder-only models, may inadvertently create an unnatural test set that does not reflect real-world scenarios. It's unclear why a simpler approach of always treating the older version as original and the newer version as perturbed was not consistently used, especially given that the authors state the perturbations are natural and occur over time. This raises concerns about the validity of the test set and the generalizability of the findings.

### Questions
line 334-337: I have trouble understanding this long sentence with too many clauses. can you explain that?

### Soundness
3

### Presentation
3

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
The authors study the impact of real world perturbations on MRC performance for various Transformer-based architectures. They propose a framework to create naturally-perturbed test sets from popular QA datasets using the revision history of Wikipedia. They perform experiments and analyses on the abovementioned models, followed by adversarial training of encoder-only models.

### Strengths
* Comprehensive evaluation across multiple architecture types rather than only decoder models and multiple models of each type: encoder, decoder, encoder-decoder models
* Somewhat comprehensive evaluation across multiple QA datasets, with caveats: see below
* Paragraphs are generally well-written and easy to understand

### Weaknesses
 **TLDR**

The authors pose an interesting question, but the execution of the study contains unexpected design decisions that are not well-justified. The exact improvement of their claimed methodology over existing work is also unclear.

**Details:**
* The authors call out the similarities between their method and Belinkov & Bisk (2018), do not make clear the differences and improvements over the latter, if any. The claimed contribution ("novel Wikipedia revision history-based framework") also does not highlight the exact improvements over simply applying Belinkov & Bisk (2018)'s method to the MRC setting, and is therefore running the risk of over-claiming. I recommend the authors revise the framing to highlight the exact contribution over Belinkov & Bisk (2018) and other prior, similar work [1, 2].
* The encoder-only models were only evaluated on SQuAD datasets to draw conclusions, with no clear justification even though the authors are aware that they are no longer challenging benchmarks. The analysis should have included a more diverse range of datasets to assess the generalizability of the findings.
* The transition to experiments on the other architectures and datasets was a little strange (only evaluating on questions that the encoder models failed on) with no clear justification. There is then a transition back to encoder-only models and SQuAD for adversarial training, also without clear justification for excluding other datasets and architectures. This creates a fragmented experimental design that makes it hard to draw consistent conclusions.
* The authors appear to have missed relevant work on robustness evaluation in QA/MRC [3, 4] and other types of synthetic perturbations [5].

### Questions
> Questions on which none of the encoder-only models fail under the perturbation are then removed.

Why was this decision made, rather than studying the effect of all perturbed questions on each architecture type? An analysis of the overlaps between architectures is good to have, but I would have preferred to see the former if I had to choose one. I may have missed a strong justification, if one has already been included.

### Soundness
2

### Presentation
3

### Contribution
2
