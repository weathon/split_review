# LLaRA: Supercharging Robot Learning Data for Vision-Language Policy

- Decision: Accept
- Scores: 6, 6, 6, 3

## Abstract
LLMs with visual inputs, \ie Vision Language Models (VLMs), have the capacity to process state information as visual-textual prompts and respond with policy decisions in text.
We propose \modelname: \textbf{L}arge \textbf{L}anguage \textbf{a}nd \textbf{R}obotics \textbf{A}ssistant, a framework that formulates robot action policy as conversations and provides improved action outputs when trained with auxiliary data that complements policy learning.
We first introduce an automated pipeline to generate \emph{conversation-style instruction tuning} data from existing behavior cloning data. 
Then we enrich the dataset in a self-supervised fashion by formulating six auxiliary tasks.
A VLM finetuned with the resulting collection of datasets can generate meaningful robot action policy decisions. Our experiments across multiple simulated and real-world environments demonstrate the state-of-the-art performance of the proposed \modelname framework.
The code, datasets, and pretrained models are available at \href{\myurl}{\myurl}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript proposes a framework for performing auxiliary instruction-tuning of LLaVA, using a robotics behavior cloning dataset that has been converted into a conversation-style instruction-tuning dataset, with the goal of enabling the model to better understand spatiotemporal context.

### Strengths
The pursuit of robotics-oriented pretext tasks for training large-capacity open source models remains quite compelling.

### Weaknesses
Section 2, Section 6: The manuscript introduces relevant contemporary approaches — some with strong inductive biases — but the experimental comparisons with the method proposed by the manuscript remain shallow. I would like to see some direct comparisons with existing VLAs in the experiments section, in addition to ablations on, e.g., different action space representations (e.g., versus RoboPoint).

Section 2 (L146-148): The manuscript states, "Moreover, all the aforementioned studies lack of comprehensive investigation into the methods for generating auxiliary datasets from existing robot data, as well as the implications of integrating such datasets." OpenVLA uses mixtures of exisisting OXE component datasets, for a next action token-prediction pretext.

Section 5: The dependency on high-quality behavior cloning data may limit LLaRA’s performance in environments significantly different from the training data. Other methods cited by the manuscript do not share this limitation.

Section 5: The pretext task proposed by this manuscript, which relies on object locations (in a tabletop coordinate system) and joint rotations will be less general than, e.g., the next-token prediction pretext and action tokenization proposed by OpenVLA. The manuscript should better motivate the reduced scope, whereas many of the models mentioned in Section 2 pursue general training and execution paradigms: across domains, embodiment, and task families.

### Questions
No additional questions — please see above.

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
4

### Summary
The paper aims to transform behavior cloning data into a form that is more accessible for VLM training, enabling the VLM to leverage its pretraining for downstream tasks. The approach involves converting the BC dataset into image-text data and having the model output 2D coordinates rather than the 3D outputs. The study introduces curated datasets to assist in 2D grounding, action prediction, next observation prediction, and understanding spatial relationships between objects. The model is evaluated against RT-2 and VIMA, showing performance gains, particularly in low-data regimes.

### Strengths
- The paper reformulates BC data into an image-text format compatible with VLMs. This is not a new idea (RT-2), but they do introduce a new output space and auxiliary objectives. 
- Restricting output to 2D coordinates sets the model apart from prior 3D-focused models like RT-2, aligning well with tasks where 3D positioning is unnecessary. Various curated datasets support 2D grounding and action prediction, aiding spatial and relational understanding. 
- The model outperforms versions of VIMA and RT-2, particularly in low-data settings.
- They show gains on simulation and real tasks.

### Weaknesses
It was not directly clear to me which components contribute to performance in the RT-2 and VIMA comparison. RT-2 also uses auxiliary tasks and internet data; it's unclear how the proposed auxiliary tasks compares. An ablation of the auxiliary tasks used in RT-2 versus LLaRA would help isolate the contribution of each component. Specifically, it is unclear how the self-supervised auxiliary tasks, which are derived from the robot's own trajectories, compare to the internet-sourced VQA and captioning data used in RT-2. The paper does not provide a direct comparison of these two types of auxiliary data, making it difficult to assess the unique benefits of the proposed approach. The lack of clarity on the specific types of auxiliary data used in RT-2 makes it difficult to isolate the contribution of LLaRA's self-supervised approach. 
- The contributions of each dataset are unclear; a more interpretable format is needed to highlight key influences on performance. The paper does not provide a clear breakdown of how each curated dataset contributes to the overall performance gains. For example, it is not clear which datasets are most critical for 2D grounding, action prediction, or spatial reasoning. A more detailed analysis, perhaps through a per-dataset ablation study, is needed to understand the impact of each dataset on different aspects of model performance. Without this, it is difficult to understand the relative importance of each dataset and how they interact to achieve the reported results.

### Questions
- RT-2 also co-trains on auxillary tasks and internet data. How does this compare to the proposed approach?
- For the comparison with VIMA, can additional insights be provided on which specific modeling choices (beyond single-view versus dual-view inputs) contribute to LLaRA’s superior performance?
- Can the comparisons with RT-2 and VIMA be unified to allow for a clearer, combined comparison?
- More analysis on Figure 6 is needed to understand the dataset contribution. Which datasets contribute most? A visualization or table that clearly shows the impact of each dataset on different aspects of model performance would be helpful.
- Is the primary difference between LLaRA and the RT-2 baseline solely the output token space?

### Soundness
3

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
The authors introduce a mechanism for (1) leveraging VLMs for robot task completion and (2) augmentation of trajectories with object/task auxiliary data.

### Strengths
They present these results on both a simulated and physical benchmark. The paper also includes a substantial set of results in the appendix.

### Weaknesses
I'm concerned about the generality of the work, based in large part on the inconclusive trends presented.  I'll provide a series of questions below but my primary concern is that it's unclear on training.  It appears that training either has no effect or hurts performance in most cases.  There's some improvement when two epochs are run (in some conditions, but not all).  Similarly, how much data and when/where/why it helps are unclear.  This doesn't detract from the fact that a nice system was deployed but it does make it difficult to determine where this research leads in the future.

There's work on the limitations of numerical representations in transformers.  Presumably this means we should see failure cases due to misunderstanding in this work, can the authors provide those examples or justify why they wouldn't occur in this domain?

Are the augmentations validated for correctness?

Can Fig 5 be augmented with another plot that show how many training samples (not just trajectories) each approach has?

Why was 12% chosen (e.g. Table 1), is that simply the first time the model outperforms VIMA? Do the results plateau afterwards? 

Fig 6, small confirmation that the X-axis means "2x, 4x, ..." ?

L434: What's the coverage on 0-180 [sort of related to question #2]

JT is worse than FT, why? -- similar confusion or missing justifications for Tables 18/19

### Questions
1. See weakness discussion
2. There's work on the limitations of numerical representations in transformers.  Presumably this means we should see failure cases due to misunderstanding in this work, can the authors provide those examples or justify why they wouldn't occur in this domain?
3. Are the augmentations validated for correctness?
4. Can Fig 5 be augmented with another plot that show how many training samples (not just trajectories) each approach has?
5. Why was 12% chosen (e.g. Table 1), is that simply the first time the model outperforms VIMA? Do the results plateau afterwards? 
6. Fig 6, small confirmation that the X-axis means "2x, 4x, ..." ?
7. L434: What's the coverage on 0-180 [sort of related to question #2]
8. JT is worse than FT, why? -- similar confusion or missing justifications for Tables 18/19

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose to fine-tune an LLM into a robot policy by formatting robot decision-making as textual “conversations.” They provide an automated pipeline for converting existing demonstration data into their expected conversational text format. Additionally, they augment that dataset with additional helpful features, such as object bounding boxes extracted from some other vision model / simulation ground truth.

### Strengths
- LLaRA seems well-motivated, given recent interest in fine-tuning (V)LMs for control
- It seems to make intuitive sense that, if you’re starting from an instruction-following “conversational” policy, you’d want to fine-tune it to similarly respond to “conversations.” 
  - That said, the extent to which this is the case is unclear: see questions.
- The authors communicate the format of their data and tasks extremely well, providing extensive examples.

### Weaknesses
 **PLEASE READ MY FOLLOW-UP COMMENT.**

**[IGNORE] This paper is extremely similar to [Embodied Chain-of-Thought Reasoning (ECoT)]**, which precedes this work (being accepted at CoRL 2024) and goes uncited in the paper. For reference:
- **[IGNORE]** ECoT also proposes to format useful features for robot control into a string, then fine-tune a vision-language model into a robot policy that predicts said strings.
  - The paper does not explicitly state they formulate robot control as “chat,” but as reasoning instead.
  - However, this seems to be a somewhat superficial distinction; the only difference is the extent to which the “reasoning” is dressed up as a conversation. It is unclear if there’s a reason that one format would be better than another.
- **[IGNORE]** As with this paper, the ECoT authors propose to extract e.g., bounding boxes, which serve as an intermediate feature which the model predicts.
  - A minor difference is that ECoT always predicts the bounding boxes as part of generating its reasoning and action, whereas LLaRA requires a separate call of the model (if I am understanding Appendix A.3 correctly), which may introduce additional system complexity. In either case, both ECoT and LLaRA can accept detections from other models as well.
- **[IGNORE]** Both papers use pretrained models to "supercharge" robot demo datasets with additional automatically-generated synthetic annotations. 
  - **[IGNORE]** While the reasoning steps employed by ECoT are not identical to the auxiliary datasets in LLaRA, a lot of the ones in the latter seem either simpler than the ones in ECoT (e.g., the future prediction step does not require reasoning by an external model, just formatting of existing data into a template / rephrased variations thereof) or are intractable or not robustly detectable in the real world with careful human annotation (action prediction, temporal prediction both are only easy if you have simulator state information).
  - In contrast, all experiments in ECoT were done in the real world, and all features and reasoning steps were extracted via pretrained foundation models. While noisy, the authors of that paper nonetheless showed empirical improvement in having the policy predict those features.
  - Additionally, ECoT demonstrates their pipeline on the Bridge dataset, which is much more representative of existing real-world robot demo datasets (with other datasets in collaborative efforts like Open-X-Embodiment having similar structure). As the BC datasets considered by LLaRA only do 2D pick-and-place high-level actions, it seems unclear if this will be practical for the more complex kinds of actions present in e.g., OXE again.

**Likewise, most of the limitations mentioned in the appendix seem to be addressed by the ECoT paper:**
> First, some concepts in the reference images still can not be easily and precisely described by language, while in many cases these features are critical for robot control. Due to the single image limit of the current VLM, we still rely on the object detector trained on a limited number of classes to describe the additional images in the task description, which limits the generalization ability of this method.

- **[IGNORE the first part, but the second part is still applicable]** ECoT specifies that they use a VLM scene captioner and open-vocabulary bounding box generator to circumvent this. This does not completely remove the issue that some scenes are just naturally hard to describe in language, but at least removes the limitation of using object detectors trained on a limited number of classes.

> Second, the information extracted from the dataset can be noisy, which may lead to model confusion. In Tab. 5, there are discrepancies such as the location of an object in a reference image differing from its actual location in the current image observation. 

- **[IGNORE]** ECoT seems like it would be much less susceptible to noisy labels, since it’s just conditioning on them, rather than relying on them to exactly determine the action (parametrized by pixel coordinates that seem to be precisely dependent on the detected position of objects).
- **[IGNORE]** All main experiments in ECoT were conducted in the real world, where one must expect there to always be more noise than in simulation. It thus seems like said approach seems robust to the noise.
- Likewise, the real-world experiments for LLaRA seem very limited. In particular, from the examples shown in Table 13, it seems like all real world tasks can be completed by simply copying the values from the detector:
  - “Rotate the <obj>.at <x, y> by <r> degrees” is correctly solved by the command “Pick <obj> at <x, y>, rotate <r>”
  - “Put <obj1> at <x1, y1> on top of <obj2> at <x2, y2>” is correctly solved by the command “Pick <obj1> at <x1, y1>, rotate 0, place at <x2, y2>”
  - Given that no complex spatial reasoning is needed here, this seems like an insufficient demo of LLaRA’s performance.
  - It is likewise unclear why LLaRA pretrained in sim doesn’t succeed at this, or why LLaRA trained on real-world data doesn’t get 100% (intuitively the task seems exceedingly easy, since it just involves copying values?)

> Finally, our method relies on 2D to 2D mapping to convert image coordinates into actual actions, which may face challenges when the complex 3D movement of the robot is required. We believe enhancements in the mentioned aspects could further improve performance and broader applicability in complex, real-world applications.

- **[IGNORE]** ECoT states that they adopt the same tokenization scheme as OpenVLA / RT-2, which is significantly more expressive than the pick-and-place actions parametrized by start and end 2D location and rotations.
- Some of the tasks they test on seem to be very hard to express in the simple 2D-to-2D action parameterization used in LLaRA (e.g., wiping); it thus seems clearly important to demonstrate approaches that work well with such action representations (the “RT-2 style,” as named in the paper), but there is limited evidence that LLaRA could do so, especially since so much of it seems inherently tied to the simplified 2D-to-2D case (e.g., expressing 3D rotations in language is much more unwieldy than the 2D rotation case presented in this paper).
- Additionally, unless I am misunderstanding, LLaRA seems to only consider cases where tasks can be solved by a handful of 2D pick-and-place actions (with the real world experiments seemingly only to require one per episode). In the execution of that one action, the robot seems to be open-loop (that is, it cannot detect failure over the course of a single pick-and-place action, only before and after -- please correct me if I am misunderstanding). **[IGNORE]** In contrast, since ECoT uses "lower-level" actions, it can detect, reason about, and correct mistakes earlier.

**Given all this, it is unclear if LLaRA makes significant contributions over ECoT.** As discussed above, there are certainly subtle differences between the two approaches, but many of those differences seem to either be design choices or in ECoT's favor.

### Questions
**[All questions should NOT be ignored, they still apply.]** 
- Why does sim LLaRA fail at the real-world tasks, if they seem to be so easy? Why doesn’t fine-tuned LLaRA achieve near 100% success, except in the last row of the FT section of Table 3?
- Does LLaRA ever experience e.g., failure to grasp, object slipping from gripper, or other similar failure cases in sim, and if so, is it able to recover?
- Similarly, it looks like in Table 5, LLaRA is trained on text traces that say “you have completed __.” Does it have to predict this itself, or is it just assumed that, after executing an earlier step, that step was successful, and so it can go in the action history?
  - If that’s the case, that seems to be another weakness compared to ECoT, as the latter approach has a reasoning step that determines which step of the plan it generated it should try to execute given the current observation. Thus, if it observes a failure case, it can return to and older step to try again
- A big point of ECoT (and even non-reasoning works that train a VLM into a robot policy, like OpenVLA) is that the VLM provides good visuo-semantic representations that could be useful for robots, especially for generalization. Is this observed by LLaRA, and if so, how / to what extent?
  - "In general, LLaRA demonstrates a robust capacity for generalization. Our observations confirm that it takes much less effort and data to transfer LLaRA models pretrained on simulated VIMA data to a real-world domain"
- Did formatting things as conversations actually help in some way, rather than just formatting in general (potentially templated) language? It seems like the conversational responses are nonetheless very structured and templated, so it’s unclear to me how much the VLM’s conversational abilities are retained (or even matter for pretraining).
- More broadly, did formatting things in natural language make a difference? What happens if the policy's response was always just in action tokens, akin to the RT-2-style?
  - Related: Did RT-2-style have the same expressivity as your approach? Since you're outputting <x, y> coordinates as string representations of floating points, it seems like your approach needs more tokens than what RT-2-style policies are even allowed to output. Since you output the rotation in degrees (from -359 to 359), it seems unfair to give RT-2 only a single rotation token with 256 bins. That seems to artificially make RT-2-style policies less expressive than yours.
- Similarly, what were the failure cases of RT-2 style? How did it achieve literally 0 across all real-world tests? Likewise, what were the empirical qualitative failures that made it work less well in simulation as well? As it stands, it seems to me that one such reason would be that, by expressing object positions and motions in the same coordinate system, it becomes artificially easier, since the VLM backbone may have a strong bias to being able to just learn to copy the object coordinates as the action parameters.
- Related: it seems like having prompts like "Place the object at <coordinates> in the bowl at <coordinates>" makes things a lot easier (when you've got a good object detector), especially when your actions are specifically parameterized in that coordinate space. What happens when you remove the coordinates in the prompt? This is important to test, since 2D pick-and-place of this form is one of the few robotics settings where that mapping from object coordinates to action coordinates is extremely trivial; most realistic robot learning applications will not be like that.

### Soundness
2

### Presentation
3

### Contribution
1
