# Latent Action Pretraining from Videos

- Decision: Accept
- Avg Score: 5.83
- Scores: 6, 6, 8, 6, 3, 6

## Abstract
We introduce Latent Action Pretraining for general Action models (LAPA), an unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a \textit{latent} VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation model. We open-source the model checkpoints and code at \href{https://latentactionpretraining.io/}{latentactionpretraining.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes an unsupervised pre-training method, LAPA, for vision-language-action (VLA) models that eliminates the need for action labels. LAPA uses a VQ-VAE structure to learn quantized action latents from frame differences. Subsequently, the authors train a VLA model to predict these quantized latents based on frames and language instructions. This model can then be fine-tuned on small-scale robot manipulation datasets. Through experiments on both simulated and real-world datasets, LAPA demonstrates improved performance over selected baseline models to indicate its generalization ability.

### Strengths
Originality:
- The proposed method removes the need of action labels for pre-training VLA models which significantly increase the data availability.
- Training VQ to predict delta between frames is a simple and scalable way of learning coarse latent action. 
- A significant performance improvement compared to SoTA (OpenVLA) model under various scenarios and relatively small performance gap between the upper bound case (ActionVLA) and LAPA. 

Quality:
- The proposed method is technically sound.
- Extensive experiments are conducted to evaluate LAPA performance under various scenarios.

Clarity:
- The paper is overall well-written and easy to follow.

Significance:
- LAPA provides a way of utilizing large amounts of videos without action labels with huge embodiment distribution shifts, which is a significant contribution to scalable robot learning.

### Weaknesses
 - Lack of Experiments on Sequence Length in VQ Stage: There is a lack of experiments illustrating the effect of different sequence lengths during the VQ stage. It seems arbitrary that the latent code length is set to 4 (line 433-434), and for the language table dataset (line 933), the sequence length is set to 1. A discussion on the rationale behind these choices is missing. Incorporating experiments on various sequence lengths could help assess LAPA’s flexibility and robustness.

- Limited Ability to Capture Complex Movements: Learning frame differences may only capture simple movement information. In visualizations of the learned latents, it appears that LAPA’s latent code primarily contains embodiment or camera movement information. Detailed results (Tables 13, 14, and 15) also indicate that LAPA performs better on coarse movement tasks like knocking and covering but struggles with finer actions like grasping or picking objects. This suggests that frame-difference learning might not be ideal for learning action latents. Including experiments with alternative approaches could provide a clearer evaluation. 

- Impact of Smaller Action Space: The smaller action space in LAPA compared to OpenVLA (256 bins for each action dimension in OpenVLA vs. a relatively smaller space in LAPA) may account for the observed performance improvement, rather than frame-difference learning alone. Reducing OpenVLA’s latent space for fairer comparison could better clarify the contributions of each part of LAPA.

- Minor Wording Issue: The phrase “actionless video” on line 83 may be misleading, as it implies the absence of any action. Consider rephrasing for clarity.

### Questions
- Need clarification for pretraining stage: In table 1, authors provide details about the dataset for both pre-train and finetune phase, however, it remains unclear about the latent action quantization. My understanding is that latent action quantization is part of the pretraining so both latent quantization  (section 3.1) and latent pretraining (section 3.2) use the same dataset. Clarification of the dataset usage could provide a better understanding of the experiment set up. 

- In most of the experiments, LAPA is trained with a single large scale dataset for fair comparison with other models like OpenVLA. Since LAPA does not require any action label during pre-training, it would be interesting to see having all three datasets used together can provide benefit of downstream performance boost to further backup the scalable claim.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel pretraining method for VLAs. It first utilizes VQ-VAE to learn a encoder which encode the image into discrete token, and the decoder decode the next frame to learn the dyanmics of the adjacent frames. The discrete tokens could be treated as action tokens and replace the action labels in the human / robot rollouts.
The authors conduct  successive experiments to demonstrate the model's performance over in-domain scenes, cross-env scenes and cross embodiment scenairos to demonstrate the effectiveness of the proposed framework.

### Strengths
The innovative approach of using VQ-VAE to encode image dynamics into latent space and replacing labeled actions with these encoded tokens is particularly intriguing. This method holds significant importance for the research community, given the high costs associated with data collection for action labeling.

The experimental validation is comprehensive, with strong results obtained from both simulation environments and real-world settings, underscoring the reliability of the model. 

The analysis is comprehensive, including the performance of in-domain, cross-environment and cross-embodiment setting.

The paper is well-structured and presented, making it easy for readers to follow the rationale and outcomes of the research.

### Weaknesses
The pretraining and finetuning setups in experiment section is a little confusing. For example, how is ActionVLA pretrained with action labels while there does not exist action labels in in something V2.

The utilized finetuning recipe of other baselines is not demonstrated in detail, which makes me concer the fairness of the comparison. I hope the authors could add detailed information in the appendix.

All the experiments in simulators are trained with only few trajectories, especially in Bridge V2, only 100 trajectories are utilized. I am wondering that if the model could learn multiple language conditioned tasks (like above 30 categories with diverse instruction) well. I am concerned that the limited number of trajectories might not be sufficient to demonstrate the model's ability to generalize to a wide range of language-conditioned tasks. I suggests that tha authors add more experiments in a new simulator with more task catigories, and further train with RT-X data mixup and test the model performance in Simpler with Bridge and Google Robot.

### Questions
See weakness.

### Soundness
4

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
4

### Summary
This paper proposes a method to pretrain vision-language-action (VLA) models for robotic manipulation using video data without robot action labels. Starting with actionless videos, they first train a VQVAE to infer latent actions between consecutive frames. They then train a VLM to predict these latent actions based on the current image and the language instruction. Finally, they finetune this model using robot trajectories with action labels for the target tasks. Their approach is evaluated in simulated and real-world multi-task experiment settings, including pretraining on actionless robot videos followed by finetuning on  robot trajectories of different tasks and pretraining on human videos from the Something-Something-v2 dataset.

### Strengths
- Interesting approach: The proposed approach is both simple and practical, potentially easier to implement than the baselines considered in the experimental section. Pretraining VLAs on actionless data, especially human videos, is particularly relevant, and the use of inferred latent actions is a sensible solution.
- Good experimental results: Through extensive comparative and ablation studies in both simulation and real-world robot settings, the authors clearly demonstrate the effectiveness of their proposed method. The experiments involving pretraining on human videos are impressive.
- Clarity: The paper is well-written, clear, and easy to follow.

### Weaknesses
Since the latent actions are not directly used for downstream control and the model is finetuned on robot action labels, it’s unclear whether the performance gains come from leveraging temporal information/action priors in videos or simply from pretraining on data (robot trajectories/SSv2) that more closely aligns with the finetuning robot data compared to the base VLM’s original training data. Would a pretraining task without temporal information—such as image captioning— achieve similar results? For the same reason, it remains unclear if this approach can scale effectively to internet-scale video datasets, in particular beyond manipulation videos, as claimed by the authors.

### Questions
- Where do you think the performance gains by pretraining on videos come from (see above) ? 
- Have you tried pretraining on human video datasets other than SSv2, such as EpicKitchens, Ego4d, or even datasets less focused on manipulation ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents LAPA, a method that aims to bridge the human-to-robot embodiment gap for VLA model training. 
LAPA consists of two stages. In the first stage, an encoder-decoder transformer learns a latent action representation from actionless videos with a VAE reconstruction loss. In the second state, given a current observation and task label, a VLM is trained to predict the learned latent actions from stage 1. The model is finetuned on a small in-domain dataset to transfer the model to actual robot actions.

The authors evaluate LAPA in two simulated environments, LanguageTable and Simpler, and a real-robot setup. They show their method outperforms similar action-less baselines while being competitive with VLAs trained on large-scale action-annotated datasets.

### Strengths
- The paper is well-motivated and tackles a very important problem in Robot Learning
- The authors conduct several experiments in different environments while also including real-robot experiments
- Combining learned latent actions with VLAs has not been explored before and is an interesting approach to bridging the human-robot embodiment gap.
- The authors show that their pretraining strategy outperforms a recent state-of-the-art VLA trained explicitly with action labels.
- The authors extend on [1] and show that latent action generation can be conditioned on language, enabling a more intuitive way to generate actions than codebook action generation.


[1] Genie: Generative Interactive Environments, Bruce et al., 2022

### Weaknesses
The main weakness of the paper is its clarity.

- It is not obvious throughout the paper that LAPA uses two distinct models.  The phrasing in the introduction, ‘LAPA has two pretraining stages…' gives the impression that you use one model for both latent action representation learning and action prediction. I would clarify early on that the method consists of two distinct models.
- You refer to a learned world model in the introduction, but it is unclear where a world model is learned from the introduction.
- The method section is oversimplified and hard to understand.
    - In the text, you write that the Latent Action Quantization Model encoder produces a latent action $z_t$ for observation $x_t$, fed into the decoder. The referenced Figure 9 says that the decoder is conditioned on $x_t$ and $z_{t+H}$
    - The VQ-VAE objective is not explained clearly. Although it is mainly based on prior work, it presents a large part of the method. Thus, I would recommend explaining the objective and the resulting latent action learned in more detail. For instance, you mention $z_t$ being a sequence $s$. How is the sequence length chosen? Does the model learn to predict $s$ latent actions at once? How is the vocabulary space $C$ chosen?
    - You mention that you pretrain a VLM in Line 178. This indicates that it is trained from scratch, although you use an already pretrained model.
    - In Line 194, you mention that the latent action head is a single mlp layer. This should be mentioned in the previous section.
    - Using the abbreviation LAPA for the method and the model is confusing throughout the method section. Although you mention this at the beginning, this might be confusing for the reader. In Figure 2, LAPA is used to generate actions. In the text, you mention that LAPA trains both a world model and a policy. This isn't very clear.
    - I think a more detailed Method (Architecture) figure than Figure 2 could help better understand the proposed method.
- Although the extensive experiments and evaluations are good, the result section is too large. I would recommend cutting down here. Often, you just state the results from the table.
- To improve the paper's clarity, I would reduce the results section and instead extend the method section.

While the number of experiments is sufficient, I believe the focus could be improved. The experiment section emphasizes pretraining with large amounts of robot data where actions are available. However, in my opinion, the more interesting aspect is the pretraining step using real-world data. I would recommend shifting more attention to this area.
I would also give more details on the real-world evaluation in the main part of the paper regarding the generalization of the method. For instance, do you use the VLA to perform the task on unseen objects? I know you show this in the appendix, but these results should be highlighted in the main part of the paper.

Regarding the data scaling ablation, whether the experiment refers to finetuning or pretraining data is unclear. If it relates to pretraining data, an additional ablation regarding finetuning data would be interesting. After all, the method's goal is to enable transfer with a small amount of in-domain demonstrations.


Typos and other formatting errors:

- Line 25: Missing s in ‘model’
- Line 71: Bridgev2 missing citation
- Line 83: video missing s
- Missing axis labels in Figure 6.
- Appendix A Typo in Heading
- Table 10: Wrong tasks. Unless you modified the simpler tasks, the tasks should be Carrot2Plate and Spoon2Towel.

Overall, the paper's results are very promising, and the method applied to complex robot control is novel and interesting. Still, I think the clarity and presentation of the paper and results could be improved significantly, which would increase the contribution and relevance to the field.

### Questions
See above. Also:

- Why do you not evaluate OpenVLA on Simpler?
- Why do you not evaluate pertaining on something-something in LangTable?
- How does the framework perform with less finetuning data?
- How is the fixed window size H determined? What granularity do the produced actions have?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims to pretrain a Vision Language Action model on large scale internet video datasets.

Four stage pipeline:
1) Learn a codebook for latent actions from raw videos
2) Pseudolabel a large dataset with these latent actions
3) Pretrain a VLM on this pseudolabeled dataset to predict these latent actions
4) Finetune the latent pretrained VLM on real labeled actions

Experiments are performed in several simulated and real domains to demonstrate that LAPA can recover most of the performance of the same model architecture / finetuning setup trained on labeled versions of the pretraining dataset.

### Strengths
Paper provides
 - A new recipe for training Vision Language Action models that can use data without action labels
 - A new foundation model that seems to produce good results when finetuned on real world tasks, including state of the art results on 2/3 real robot tasks involving gross motor skills

Paper performs a number of experiments that provide hints at good performance when pretraining on unlabeled human data.

### Weaknesses
## Review

### summary:
 This work aims to pretrain a Vision Language Action model on large scale internet video datasets.

Four stage pipeline:
1) Learn a codebook for latent actions from raw videos
2) Pseudolabel a large dataset with these latent actions
3) Pretrain a VLM on this pseudolabeled dataset to predict these latent actions
4) Finetune the latent pretrained VLM on real labeled actions

Experiments are performed in several simulated and real domains to demonstrate that LAPA can recover most of the performance of the same model architecture / finetuning setup trained on labeled versions of the pretraining dataset.

### soundness:
 2

### presentation:
 2

### contribution:
 3

### strengths:
 Paper provides
 - A new recipe for training Vision Language Action models that can use data without action labels
 - A new foundation model that seems to produce good results when finetuned on real world tasks, including state of the art results on 2/3 real robot tasks involving gross motor skills

Paper performs a number of experiments that provide hints at good performance when pretraining on unlabeled human data.

### weaknesses:
 **TL;DR: There are data consistency issues throughout the paper, including in key result figures. With those fixes, method's proposed cross embodiment training recipe appears weak on actual cross embodiment data.**

**Data consistency issues**

Table 15 does not agree with the bar values in Figure 4 and 5 --- the superior performance of LAPA (Bridge) to ActionVLA (Bridge) is caused by swapping of values for ActionVLA and LAPA in the _Pick_ task, based on Table 15's results. Fixing this error makes LAPA (Bridge) worse than ActionVLA (Bridge), which is what one should reasonably expect given LAPA is unsupervised and ActionVLA is supervised and both use the same architecture. Quite honestly I think this should have been caught in a simple sanity check by the authors, as these results don't make much sense otherwise.

Table highlighting of results seem to also consistently have errors
 - In Table 4, Block2BlockRelative, VPT has its score of 48 underlined (to indicate second place) when LAPA scored 52.0
 - In Table 7, row "Separate", ActionVLA has its score of 82.0 underlined (to indicate second place) when VPT scored 84.0

These are just the most obvious issues, I cannot be certain there are not deeper issues with the results. _Given the glaring nature of the errors in headline result plots, it makes me not trust the quantitative results of the authors._

As a personal note, I want to underscore that this is not the sole responsibility of the junior authors who likely prepared the manuscript and made the plots --- at least some of these errors are ones that could (and should) have been caught by senior authors reading the paper and skimming key results. 

**Most studies are robot to robot, providing limited signal on the value of actual cross embodiment training protocol**

These studies are robot to robot tasks, which don't address the question of usefulness of pretraining on domains where we aren't able to get action labels --- it's unreasonable to assume we don't have access to the actions associated with the observations for robot pretraining data. These ablations can be informative as "Supplemental Experiments", but we need to see the action codebook, pretrained on datasets where we do _not_ reasonably have access to actions, is providing real value. 

Experiments that fall into this category
 - The Language Table experiments are robot -> robot, and these are _very_ similar tasks
 - BridgeV2 -> SIMPLER is a larger gap, it's still robot -> robot

**Studies on nonrobot to robot transfer provide weak proof of value**

Assuming the label swapping issue only impacted LAPA (Bridge)'s Pick and Place performance and nothing else (I did not check the correctness other entries in the other tables), ActionVLA trained on the 54k trajectories of Bridgev2 outperforms LAPA pretrained on the 220K human videos. Notably, 54k trajectories is quite small; OpenX has over 1 million, but ActionVLA pretrained on OpenX is an important missing as a baseline from the results --- we need to tease out architecrture differences compared OpenVLA, as LAPA uses LWM-Chat-1M (taken directly from Liu et al 2024) which appears to be superior to OpenVLA's architecture --- but all (corrected) evidence seems to indicate that ActionVLA (OpenX) will not do worse than LAPA (OpenX).

Clearly pretraining on human data is not expected to match training on labeled robot data on a sample vs sample basis, but to make the argument that this pretraining is providing value, we need to see scaling laws showing that increased human data translates to increased performance; unfortunately, the authors made the puzzling decision to run their scaling laws experiments on Bridge (an already small dataset), instead of the salient dataset to this question, so we have no way of knowing how the method improves with data scale. 

Given how the unsupervised action encoder works and the human hand latent analysis in Appendix E / Figure 15, my hypothesis is that if the task distribution of the human dataset (Table 3) remains the same, the gross motor base latent actions are still going to be discovered pretty early on and the marginal value of each additional sequence will quickly approach zero --- this of course needs to be verified or falsified, but there's no evidence in the paper to do that.

**Actionable feedback**

1) Please go review all of the numbers in detail from top to bottom. I happened to catch some of these issues, I have no idea how many more are hidden.
2) I think the ideas presented here are interesting, but the story being told needs to be significantly refined. Pretraining on the human data needs to be front and center, and there needs to be a focus on performance as we scale up this dataset
3) ActionVLM pretrained on OpenX is a useful artifact on its own. I don't know if someone's done this already or not, but such a release itself would be useful to the community.

**UPDATE NOV 24th**

In light of the authors' comments on the correctness of Figures 3 and 4 I have raised my score from 1 to a 3. The remaining issues, related to the fundamental story of the paper, are detailed in my responses to the authors' comments.

### questions:
 1) What exactly are the error bars on all the plots? Standard deviation? Standard error? I didn't see it anywhere listed.
2) In Figure 4 and 5, is there a reason ActionVLA (OpenX) is not included?

Nitpicks:

Section 3 needs polish so that it's easier to read
 - Figure 2 is missing a label on step 3 for finetuning
 - e.g. on line 177/178, "label all $x_t$, given $x_{t+1}$, with $z_t$" ->  with "label all frames $x_t$, given frame $x_{t+1}$, with latent action $z_t$". If you're trying to skim, you have to go back to Section 3.1 to figure out the definitions of these math symbols.

Figure 5 needs to have its colors made consistent between subfigure a and b; right now it looks like VPT, which is pink in figure a, is appearing in figure b

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

----

## Round 1: Review

**It is unreasonable to assert that LAPA (OpenX) outperforms OpenVLA (OpenX) because LAPA's training regime is better.**
 - The **critical baseline of ActionVLA (OpenX) is missing**, so we cannot know if this is due to the architecture or due to the training recipe
 - The standard error bars overlap, so it's not reasonable to assert victory, and this is not a nitpick when you consider the noise of the underlying eval (few tasks, few trials)

Unless you can produce results for ActionVLA (OpenX), I remain unconvinced that LAPA's training regime is better than supervision from OpenX's action labels.

**Your Something Something v2 10% scaling datapoint is uninformative.** You saw 2% success improvements scaling up the pretraining dataset size 10x. On it's face that would look like saturation, but we cannot know for sure and it's your job to provide evidence it's not.

**Bridge cross-embodiment results do not clearly legitimize LAPA**. Bridge is a relatively tiny dataset, and the fact that both LAPA and ActionVLA perform equally poorly can as much be attributed to dataset size as the relative merit of LAPA.

**You are missing scaling laws so you cannot claim your method "paves the way to internet scale data"**. I have made my position on this clear, and I hope the AC is reading closely enough to not just listen to slogans. Indeed, no one seems to have yet cracked the code for pretraining policies; even the recent paper from Physical Intelligence [1] seems to have broadly negative results for pretraining: despite using datasets 10x larger than OpenX, in Figure 11 they are hardly able to beat training from scratch in-domain. 

If you want to legitimately make the claim that LAPA is paving the way to internet scale data, you need to provide evidence for that. I have made it clear that, as written, **this paper must show scaling performance to substantiate its rhetoric**. If the authors lack the compute resources to run that experiment, then the paper must be rewritten with more modest framing.

Unless my concerns are addressed, I will keep my rating of 3 and ask that other reviewers please reconsider their ratings for acceptance due to these important missing experiments. This paper as written does not provide value to the robot learning community, and unfortunately given the 10% Something Something V2 performance and the way the method works, I personally suspect that the method simply does not serve as a good mechanism to do pretraining on internet data, which is the entire reason this work is supposed to be interesting.

[1] Black et al. π0: A Vision-Language-Action Flow Model for General Robot Control. 2024 https://www.physicalintelligence.company/download/pi0.pdf

### Questions
1) What exactly are the error bars on all the plots? Standard deviation? Standard error? I didn't see it anywhere listed.
2) In Figure 4 and 5, is there a reason ActionVLA (OpenX) is not included?

Nitpicks:

Section 3 needs polish so that it's easier to read
 - Figure 2 is missing a label on step 3 for finetuning
 - e.g. on line 177/178, "label all $x_t$, given $x_{t+1}$, with $z_t$" ->  with "label all frames $x_t$, given frame $x_{t+1}$, with latent action $z_t$". If you're trying to skim, you have to go back to Section 3.1 to figure out the definitions of these math symbols.

Figure 5 needs to have its colors made consistent between subfigure a and b; right now it looks like VPT, which is pink in figure a, is appearing in figure b

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an unsupervised method for learning action knowledge from internet-scale video data. Without the need for action labels, the method implicitly models the action information contained in videos, making it possible to acquire generalizable knowledge from a vast amount of videos. The foundation model obtained from pre-training can be transferred to specific downstream robot manipulation tasks through supervised fine-tuning. The article validates the model's superiority over state-of-the-art VLA models by pre-training and fine-tuning with data from different domains.

### Strengths
The proposed unsupervised training method is highly significant. By employing VQ-VAE to learn action tokens, it is possible to model the action knowledge contained in videos without requiring action labels, which makes the pre-training with a larger scale of videos feasible for future applications.

The proposed method for reconstructing future frames during pre-training is reasonable and concise. The visualization results in the paper also confirm that the method can indeed learn structured action latent representations from unsupervised video data.

The experiments conducted in this paper are quite meticulous, including pre-training within the same domain, cross-task pre-training, as well as pre-training on large-scale real-world data like BridgeV2 and Open-X.

### Weaknesses
The method used in this paper is relatively simple. Pre-training through the prediction of future frames has been mentioned in some previous works. And the paper also points out that training directly with the VQ-VAE objective is quite similar to Genie. The ensuing question is, when the pre-trained video data is particularly abundant and spans a large number of domains, whether such a training method is sufficient to capture the patterns of action embeddings. Additionally, the selection of window size H for future frames is fixed during the training process, does such a choice bring difficulties to the modeling of actions? Could you explain the reason for choosing a fixed window size, or an ablation study on different window sizes?

The experimental validation part of the paper could be more robust. The current simulation environments use Language Table and SIMPLER, while real-world experiments only involve three tasks. How does OpenVLA perform in the simulation experiments used in this paper? And compared with OpenVLA, it does not seem to bring absolute advantages in all real-world tasks, such as "Knock" and "Cover" training with Bridge data.

### Questions
See above. I'm willing to discuss with other reviewers and authors to decide my final rating.

### Soundness
3

### Presentation
3

### Contribution
3
