# Uncovering Latent Memories in Large Language Models

- Decision: Accept
- Scores: 8, 6, 8, 3

## Abstract
Frontier AI systems are making transformative impacts across society, but such benefits are not without costs: models trained on web-scale datasets containing personal and private data raise profound concerns about data privacy and security. Language models are trained on extensive corpora including potentially sensitive or proprietary information, and the risk of data leakage, where the model response reveals pieces of such information, remains inadequately understood. Prior work has investigated that sequence complexity and the number of repetitions are the primary drivers of memorization. In this work, we examine the most vulnerable class of data: highly complex sequences that are presented only once during training. These sequences often contain the most sensitive information and pose considerable risk if memorized. By analyzing the progression of memorization for these sequences throughout training, we uncover a striking observation: many memorized sequences persist in the model's memory, exhibiting resistance to catastrophic forgetting even after just one encounter. Surprisingly, these sequences may not appear memorized immediately after their first exposure but can later be “uncovered” during training, even in the absence of subsequent exposures - a phenomenon we call "latent memorization." Latent memorization presents a serious challenge for data privacy, as sequences that seem hidden at the final checkpoint of a model may still be easily recoverable. We demonstrate how these hidden sequences can be revealed through random weight perturbations, and we introduce a diagnostic test based on cross-entropy loss to accurately identify latent memorized sequences.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the mechanics of memorization (as defined currently in LLM literature) in depth along two axes: number of repeats of a string during pretraining and complexity of string and largely focuses on high complexity strings that are exposed only once and thus, based on existing evidence, are less likely to be memorized. Based on this investigation the paper finds that (1) memorization of such strings is rather stable during training (ie there's no clear trend of catastrophic forgetting) and that (2) there is evidence of "latent" memorization, ie, sequences which the model has seen only once and seem to not be memorized, can be surfaced using simple modifications such as adding random noise to model weights. Since such latent memorization can go unnoticed by existing measures, the paper also shows that a simple evaluation of cross entropy loss on such sequences clearly shows lower loss for latent memorized sequences and could be a simple diagnostic to measure latent memorization.

### Strengths
-  The paper studies the very important problem of memorization, is well written and adds a fresh new perspective to this space. 
 -  I appreciate that the authors use carefully constructed metrics to study this rather nuanced phenomenon. I appreciate the relaxation of Carlini et al's definition using Levenshtein distance since such a measure allows for careful analysis of what factors contribute and to what degree towards memorization.
 - It was also quite nice to see complexity of string being considered a a factor. There's always the question with compressible strings whether reconstructing them given context is memorization eg: given context "aabbaabb" if one were to logically extrapolate, "aa" would likely be the next two characters. At that point I'm not sure if calling it memorization is the right thing. So I appreciate that the authors focused on strings where such extrapolations are almost impossible.
 - The result with "latent" memorization is really neat and I really liked the mechanistic approach to arrive at the method of adding noise to weights to surface the latent memorized strings. This result also has many practical implications, eg, someone taking an off the shelf base model and then finetuning the model is running the risk of having a model that can regurgitate information that was exposed during pretraining -- something the entity finetuning has likely no control over.
 - The diagnostic for latent memorization is also very neat and intuitive, I wonder if cross entropy loss should be used for measuring all kinds of memorization, since ultimately "latent" memorization is also memorization.
 - Overall I really enjoyed reading this paper. I think it provides a fresh perspective on memorization and poses many interesting questions for the field.

### Weaknesses
 - [Data statistics and memorization] I am a little confused by Section 3.1. You say "simpler strings are more easily memorized" -- but this could very well be an artifact of the checkpoints you use. Since you pick checkpoints not exactly at the beginning, I would suspect simpler kinds of in-context learning to be at play here. If strings are highly compressible (ie simpler on your z-complexity scale) I would imagine based on the "k" part of the prompt one can infer the "l" part without necessarily memorization. Secondly, your paper later on shows that this kl-LD definition of memorization can miss other kinds of memorization like latent memorization. So taking latent memorization into account, is the statement that "simpler strings are more easily memorized" still true?

 - [Stationarity of memorization] Maybe I missed this, but could you say how many tokens were seen in the window you consider for the stationarity analysis in eg Fig 2a? I wonder if stationarity is a function of how many tokens it sees in the considered window -- because surely a once-encountered string in training should have some limited shelf life? How many tokens does it take for the capacity in the model to run out to retain this latently memorized string? 

 - [Mechanics of memorization] The intuition that the somewhat strange mechanics of memorization are related to weights is really intriguing to me. However, I wonder if the statement "but this is in conflict with the fact that the model weights are constantly evolving" is super convincing. Let's run with your hypothesis that strings are encoded in model weights, then to memorize a single 64 character string you'd need 32 parameters (assuming again the float16 setting in the paper and no redundancy in encoding the string in weights) out of more than a billion parameters overall. The chances that you are changing such a small fraction of weights significantly is, I think, rather small. Not absolutely necessary for this work but maybe future work should look at how weights change when a string goes from memorized to non-memorized (as per the kl-LD definition).

 - [Mechanics of memorization] since the memorized sequence is only encountered once, I would suspect when it's encountered also plays a role in these dynamics. You consider checkpoints that are still fairly early on in training (compared to more recent models like llama/mistral which train for much longer), what would happen if this encounter happened much later on when training has matured somewhat? If we are to run with your hypothesis that this memorization is encoded in the model weights, then I would suspect as you overtrain models, the capacity to keep such rare and hard strings latently memorized would decrease. Again perhaps something to look at in future work.

 - [Recovering latent memorized strings] I really liked the idea of weight perturbations, however I wonder if you could also pull another lever here, which is the "k" part of the context given to the model. That is, it would be very cool to know if perturbing the weights is the only way to get the model to surface up these latent memorized strings and whether some kind of prompt hacking couldn't get you the desired outcome? If indeed no amount of prompt hacking can get you to the "l" part of the string then I think this will be much stronger evidence for your hypothesis of these strings being encoded in the weights.

 - [General comment] Your proposed diagnostic of latent memorization based on CE loss could also be extended for "standard" memorization, right? Is there any reason you would see to prefer the kl-LD definition?

 - [General comment] An overall comment I have about the paper is that you *could* call this entire paper a critique of existing defintions of memorization. Ultimately "latent" memorization is also memorization and perhaps we should expand our current definition of memorization to also take into account things one could get the model to output given *any* modifications (eg the weight modifications you propose). Any reason where you think the kl-LD definition for memorization is still the "better" definition?

### Questions
- [Data statistics and memorization] I am a little confused by Section 3.1. You say "simpler strings are more easily memorized" -- but this could very well be an artifact of the checkpoints you use. Since you pick checkpoints not exactly at the beginning, I would suspect simpler kinds of in-context learning to be at play here. If strings are highly compressible (ie simpler on your z-complexity scale) I would imagine based on the "k" part of the prompt one can infer the "l" part without necessarily memorization. Secondly, your paper later on shows that this kl-LD definition of memorization can miss other kinds of memorization like latent memorization. So taking latent memorization into account, is the statement that "simpler strings are more easily memorized" still true?

 - [Stationarity of memorization] Maybe I missed this, but could you say how many tokens were seen in the window you consider for the stationarity analysis in eg Fig 2a? I wonder if stationarity is a function of how many tokens it sees in the considered window -- because surely a once-encountered string in training should have some limited shelf life? How many tokens does it take for the capacity in the model to run out to retain this latently memorized string? 

 - [Mechanics of memorization] The intuition that the somewhat strange mechanics of memorization are related to weights is really intriguing to me. However, I wonder if the statement "but this is in conflict with the fact that the model weights are constantly evolving" is super convincing. Let's run with your hypothesis that strings are encoded in model weights, then to memorize a single 64 character string you'd need 32 parameters (assuming again the float16 setting in the paper and no redundancy in encoding the string in weights) out of more than a billion parameters overall. The chances that you are changing such a small fraction of weights significantly is, I think, rather small. Not absolutely necessary for this work but maybe future work should look at how weights change when a string goes from memorized to non-memorized (as per the kl-LD definition).

 - [Mechanics of memorization] since the memorized sequence is only encountered once, I would suspect when it's encountered also plays a role in these dynamics. You consider checkpoints that are still fairly early on in training (compared to more recent models like llama/mistral which train for much longer), what would happen if this encounter happened much later on when training has matured somewhat? If we are to run with your hypothesis that this memorization is encoded in the model weights, then I would suspect as you overtrain models, the capacity to keep such rare and hard strings latently memorized would decrease. Again perhaps something to look at in future work.

 - [Recovering latent memorized strings] I really liked the idea of weight perturbations, however I wonder if you could also pull another lever here, which is the "k" part of the context given to the model. That is, it would be very cool to know if perturbing the weights is the only way to get the model to surface up these latent memorized strings and whether some kind of prompt hacking couldn't get you the desired outcome? If indeed no amount of prompt hacking can get you to the "l" part of the string then I think this will be much stronger evidence for your hypothesis of these strings being encoded in the weights.

 - [General comment] Your proposed diagnostic of latent memorization based on CE loss could also be extended for "standard" memorization, right? Is there any reason you would see to prefer the kl-LD definition?

 - [General comment] An overall comment I have about the paper is that you *could* call this entire paper a critique of existing defintions of memorization. Ultimately "latent" memorization is also memorization and perhaps we should expand our current definition of memorization to also take into account things one could get the model to output given *any* modifications (eg the weight modifications you propose). Any reason where you think the kl-LD definition for memorization is still the "better" definition?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
he paper investigates the phenomenon of memorization in large language models (LLMs), specifically focusing on complex sequences encountered only once during training. The authors highlight that certain sequences, termed "latent memories," can be memorized by the model and retained persistently throughout training, even without further exposure.

### Strengths
- The concept of "latent memorization" adds a significant new layer to understanding how LLMs retain and recall data.
- Providing a diagnostic for detecting latent memorization.

### Weaknesses
 - The study primarily focuses on Pythia-1B and Amber-7B, limiting the generalizability to other, potentially larger, LLMs not tested.


### Questions
- Are there training modifications or strategies that could preemptively minimize or control latent memorization?
- How does the latent memorization phenomenon interact with fine-tuning? Would fine-tuning mitigate the presence of these latent memories?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates memorization dynamics in large language models, focusing on "latent memorization" – a phenomenon where models retain complex sequences in memory even after minimal exposure. The authors demonstrate that these sequences, initially not retrieved verbatim, can later re-emerge in model outputs through weight perturbations, raising concerns about data privacy. The paper introduces a novel diagnostic test for identifying latent memorized sequences based on cross-entropy loss and suggests potential mitigations to enhance data privacy in model training. This work adds to ongoing conversations about data leakage and highlights the emerging challenges of memory persistence in AI models.

### Strengths
- **Originality**: The concept of latent memorization and the critique of kl-memorization provide new perspectives on memorization in LLMs, advancing our understanding of potential data privacy risks. TO further substantiate the novelty, authors could consider comparing with the recent findings related to verbatim memorization mechanisms, for example,  Huang et al.  (https://arxiv.org/pdf/2407.17817)
- **Quality**: The methodology is sound, with experiments designed to isolate memorization effects. The use of weight perturbations to reveal latent memories is innovative and strengthens the study's claims.
- **Clarity**: The writing and visualizations are clear, making complex ideas accessible and well-supported by empirical evidence.
- **Significance**: The findings are relevant to privacy and security in LLMs, addressing a gap in our understanding of how sequences can be memorized and later recalled. Huang et al.'s framework on verbatim memory could provide an anchor point for discussing how latent memorization behaviors extend verbatim patterns.

### Weaknesses
 - **Scope of Evaluation**: The experiments are limited to specific language model architectures, raising questions about generalizability to other architectures and model sizes. It would be beneficial to see how the observed latent memorization effects manifest in models with different architectural choices, such as those employing attention mechanisms more heavily or those with different layer configurations. Furthermore, the study should explore a wider range of model sizes to understand if the phenomenon scales predictably or if there are critical size thresholds where latent memorization becomes more or less pronounced.
- **Mechanistic Explanation**: The authors suggest that latent memorization reflects stability in weight space, a hypothesis that could benefit from further clarification, particularly in light of Huang et al.’s findings that verbatim memorization relies on distributed states rather than specific model weights. The current explanation lacks a detailed mechanistic account of how weight perturbations specifically trigger the re-emergence of latent memories. A more thorough investigation into the specific weight parameters or network layers involved in storing and retrieving these latent sequences would strengthen the argument. It is also unclear how this stability interacts with the model's training dynamics and whether it's a general property or specific to certain training regimes.

### Questions
1. Have the authors considered how latent memorization might vary with larger or smaller model sizes?
2. Could the proposed kl-Levenshtein distance metric be generalized for other memory-intensive tasks or model architectures?
3. Are there any specific limitations to the cross-entropy diagnostic when scaling up to larger models or applying it to real-world settings?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses memorization in language models (LM) through training focusing on "latent" memorization when a model has _soft_ memorization strings during the training. The experiments measure memorization as a function of the dataset (complexity and repetitions, Figure 1), and training steps (using intermediate checkpoints, Figure 2). The paper also details a method to identify sequences that are "latent" memorized using a guess-and-check optimizer via adding random perturbations to weights and measuring memorization (Figure 4). Finally, the paper showcases that sequences with lower cross-entropy loss exhibit lower (latent) memorization.

### Strengths
- The paper discusses a fresh perspective on LM memorizing sequences with _latent_ memorization. This type of memorization feeds into the memorization at the checkpoint, which is finally considered to be deployed.

### Weaknesses
 - The main claim of the paper that memorization is stationary throughout training (Section 3.2) is largely unsubstantiated in experimental results (Figure 3). There is no trend on the sample level to make an inference. It is unclear to me what the mean line entails here. Moreover, it is difficult to parse the experiment since axes are unlabelled and not clearly discussed in the Figure 3 caption.
- The variance of memorization comparison with that of random walk is not (directly) measured experimentally and analysis in Section 3.2 is unsupported.
- It is unclear how the claim that sequences are "memorized as often as they are forgotten" (line 255 in Section 3.2) is made. 
- The assumption that the sequences with low duplication and high complexity (measured using zlib heuristic) are more likely to contain private/sensitive information makes sense, but experiments only cover latent memorization on highly complex sequences (zilb>0.8). Why not ablate on different complexity levels (like Figure 1) and see how results vary?
- The paper only focuses on syntactical memorization (Definition 2.1) with edit distance used as the only metric. It would be interesting to see the results for semantic memorization using soft embedding similar to methods like BERTScore [1].
- Adding random noise and checking if the edit distance is lower is a guess-and-check zeroth order optimization formulation. This is applied on the training/chosen dataset and thus this noise is not "random." This strongly opposes the hypothesis made that simply perturbing the weights with random noise produces similar effects as training.  
- The latent memorization is poorly defined (also not explicitly) and oftentimes read as a circular definition. For example, samples recovered from an intermediate checkpoint are latent memorized (Section 3.3) but also the other way around.
- Limited experiments in terms of model sizes. All Pythia [2] models can be evaluated to see the trends across different sizes.
- Largely, throughout the paper, the results are unsubstantiated (as mentioned above) or anecdotal (Table 2 and Line 305). The writing is unclear and difficult to parse for the reader. The aim or main conclusion of the paper is thus unsupported and unclear.

### Questions
1. Is the deduplication discussed in Section 3.2 applied to isolate the repetitions affecting memorization and focus only complexity of samples (as measured by zlib)? If so, is the same deduplication applied to training data as well (specifically for additional deduping discussed in line 244)?
1. What are the x-axis and y-axis in Figure 3a?
1. What does "the kl-LD of the sequences fluctuate (Figure 3) but do so in a way which is stationary across training" mean exactly in line 248?
1. Is latent memorization a general case of memorization (as measured by any chosen metric)?

### Soundness
2

### Presentation
1

### Contribution
1
