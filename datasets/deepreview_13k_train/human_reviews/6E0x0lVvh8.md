# Benchmarking Mental State Representations in Language Models

- Decision: Reject
- Scores: 3, 5, 3, 5

## Abstract
While numerous works have assessed the generative performance of language models (LMs) on tasks requiring Theory of Mind reasoning, research into the models' \textit{internal representation} of mental states remains limited.
Recent work has used probing to demonstrate that LMs can represent beliefs of themselves and others. 
However, these claims are accompanied by limited evaluation, making it difficult to assess how mental state representations are affected by model design and training choices.
We report an extensive benchmark with various LM types with different model sizes, fine-tuning approaches, and prompt designs to study the robustness of mental state representations and memorisation issues within the probes.
Our results show that the quality of models' internal representations of the beliefs of others increases with model size and, more crucially, with fine-tuning.
We are the first to study how prompt variations impact probing performance on theory of mind tasks. We demonstrate that models' representations are sensitive to prompt variations, even when such variations should be beneficial.
Finally, we complement previous activation editing experiments on Theory of Mind tasks and show that it is possible to improve models' reasoning performance by steering their activations without the need to train any probe.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper is a benchmark for measures of representations of agents' mental states inside LMs from the lens of probing. It studies the effect of model size, finetuning, and prompting variations on probe accuracy, and tests an activation steering method for its ability to improve the model's abilities at relevant tasks.

This work adds some experiments on top of previous probing work on the BigToM dataset.

### Strengths
* I think the paper is easy to follow, reasonably well structured, and mostly well written.
* The paper seems to include a pretty comprehensive discussion of related work.

### Weaknesses
 * The paper is on the whole a bit disjointed—a bunch of results related to theory of mind representations but without clear or enlightening takeaways as far as I can tell. I'm unclear on what is important about these results. Probing accuracy is a very weak measure of representation quality, and we want to see things like steering results to know the results are meaningful. But also: what use might come out of steering even if we do it well? Again it's unclear to me. The activation steering experiments bias the model towards correctly answering the question from the protagonist's view. But what do they do with respect to querying the oracle belief? Does it actually improve model reasoning or just bias it?
* I'm not convinced by the $k$ principal component ablation. I think if you want to show that the probing experiment is meaningful and not just a product of strong high-dimensional features then you probably want something like Hewitt and Liang (2019)'s _control tasks_ (https://aclanthology.org/D19-1275/). But better would be using the probes to do steering. Why not just include steering results for the probes?
* The description of the results at the beginning is confusing. For example: it says the paper demonstrates that the results of probing experiments are sensitive to prompting. This means nothing to me: of course the results will not be exactly the same when the prompts are different; the question is how different and if there are any interesting patterns to this. But the abstract and intro mention the results without saying anything on the matter. The sentence `We demonstrate that models’ representations are sensitive to prompt variations, even when such variations should be beneficial` is confusing—"even when" implies a contrast, but the variations being beneficial would be an example of sensitivity to prompt variation.
* The idea that the probing task on this data measures representations of theory of mind seems very questionable to me. The probe itself is specific to the protagonist of the story—but what if there are multiple protagonists? What if there is none? What's the mechanism by which the probe picks up on the representation of the protagonist's mental state and not some other correlate in the dataset like a feature of the narrative structure in the story (e.g., an indicator of someone seeing an event or missing it)? It seems to me like a weak setting for testing theory of mind. Improving the data would go a long way here I think, whereas the extra experiments in this paper tell us very little in my view.
* The point about steering vectors avoiding the need for training dedicated probes doesn't make sense to me. If you need a training dataset of positive and negative examples to compute a steering vector, you're in the exact same situation as someone training a probe—you're just using a simpler architecture and loss (i.e., your model is just a linear regressor).

### Questions
* Is there a reason you used Llama 2 instead of Llama 3? 3 has been out for a while now.
* I'm confused by RQ4, about whether the probes are memorizing their training data. Does it matter? You evaluate it on held-out test data, right? (If not, that is... bad.) That should tell you all you need to know. If you're worried that the probes are learning the task despite the LM not really knowing it, I agree this is a concern but I think you don't address it. (See my comment about control tasks under Weaknesses.)

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies probing in theory of mind (ToM) to study five research questions, including correlation between model size and probing accuracy, instruction-following fine-tuning for probing accuracy, sensitivity to prompt variations, LLM memorization for probing, and edit activations without training probes. Conducted on the BigToM across Lllama-2 and Pythia model families, results show that probing performance increases with model sizes, especially after fine-tuning. The paper also shows that using contrastive activation addition (CAA), it is possible to improve model performance without training any probe.

### Strengths
1. This paper studies five research questions related to probing language models in the context of theory of mind and conducted extensive experiments and drew insightful conclusions. This can inspire future researchers studying related tasks.
2. This paper introduces CAA, which achieves good probing performance without training any probe. This can be interesting to the community exploring probing and interpreting large language models.

### Weaknesses
1. This paper studies five research questions related to probing language models in the context of theory of mind and conducted extensive experiments and drew insightful conclusions. This can inspire future researchers studying related tasks.
2. This paper introduces CAA, which achieves good probing performance without training any probe. This can be interesting to the community exploring probing and interpreting large language models.

1. This paper raises research questions and introduces methods to probe language models motivated by theory of minds and studies specifically for ToM. However, besides the dataset used, it is not clear to see the connection to ToM. On the positive side, the proposed method can be universally applicable to general probing tasks (however, the research questions and conclusions have been extensively studied, and the methods proposed and experiments conducted do not provide additional observation to the community). On the negative side, it is not convincing that the conclusion in this paper is indeed revealing LLM's mental representations, especially when comparing to previous methods. I would suggest the authors to draw some stronger connection between the proposed research questions and experiments and ToM, and more importantly, how is it different from general probing tasks and previous methods.

### Questions
1. Why do you think CAA, by simply computing a mean difference vector, would be sufficient to serve as probing without training? Would this be able to apply to other probing tasks or is it ToM specific? Is there any trend with regard to model size, more model training, etc?

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
This paper explores the Theory of Mind performance of LLMs across various settings, specifically focusing on their internal representations to address five research questions related to model size, tuning, prompts, memorization, and inference-time intervention. Through empirical experiments, it provides valuable observations and comparative results.

### Strengths
- This work provides useful information on different LLM settings and their implications for Theory of Mind performance.
- This work conducts extensive experiments to reveal diverse behavioral aspects of LLMs in relation to Theory of Mind.

### Weaknesses
 - While these empirical results provide useful information, they do not appear to offer significant insights.
- The experiments addressing the research questions seem more like incremental extensions of previous work.
- The research questions are scattered rather than interconnected, making it difficult to grasp the main ideas of the paper.
- It would be more beneficial if the paper focused on one or two research questions and investigated them in greater depth.


### Questions
- How did the authors conduct the experiment for the pre-trained base model? Did they use few-shot demonstrations, or did they simply provide instructions, treating it the same as an instruction-tuned model?

### Soundness
2

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
4

### Summary
This paper investigates how language models (LMs) internally represent mental states, such as beliefs, in Theory of Mind (ToM) tasks. The study benchmarks multiple LMs across varying model sizes, fine-tuning methods, and prompt designs to explore the robustness of mental state representations. It addresses several research questions, including the relationship between model size and probing accuracy, the impact of fine-tuning on performance, the sensitivity of internal representations to prompt variations, and the potential risks of memorization within probes.

### Strengths
* This paper investigates how the internal representations of mental states and beliefs within language models evolve with changes in model size and training stages, providing valuable insights into the factors that influence these representations.
* The study examines how prompt variations affect the probing performance of LMs on Theory of Mind tasks, offering important findings on the sensitivity of models to different prompt designs.

### Weaknesses
1. On RQ2: The exploration of "fine-tuning with instruction-tuning and/or RLHF") is not sufficiently convincing. Different datasets and strategies for fine-tuning can lead to varying changes in the models' mental state representations. However, the paper only compares the base and chat versions of open-source models. I encourage the authors to provide a more detailed analysis in this area.

2. On Line 091 the statement "It is possible to improve models’ reasoning performance by steering their activations" may cause misunderstanding. The term reasoning here specifically refers to Theory of Mind reasoning and not to performance on tasks such as GSM8K or other general reasoning benchmarks.

### Questions
In Figure 7, the accuracy of the protagonist belief detection appears to be insensitive to variations in different prompts. You mentioned in line 431 that "LMs possess robust belief representations when taking an omniscient perspective." Could you provide more references to analyze the possible reasons for this phenomenon?

### Soundness
3

### Presentation
3

### Contribution
3
