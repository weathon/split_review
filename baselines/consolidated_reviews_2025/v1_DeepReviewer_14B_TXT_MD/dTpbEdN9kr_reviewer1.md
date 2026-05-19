### Summary

This paper presents a way to use human motion diffusion models as a prior for composition, allowing out-of-domain motion generation and efficient control. The paper presents three methods: sequential composition, parallel composition, and model composition. The first approach, sequential composition, is used to tackle the challenge of long sequence generation. The second approach is used to learn a slim communication block to coordinate interaction between two resulting motions, showing steps toward multi-person generation. The last approach is used to enable flexible and efficient fine-grained joint and trajectory-level control and editing. Using these approaches, the paper shows state-of-the-art results on HumanML3D and BABEL datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well written.
- The proposed approaches are simple and effective.
- The proposed approaches show state-of-the-art results on two datasets.

### Weaknesses

#### Some Related Works


#### comment

 - In Table 1, some of the R-precision numbers are bold that should not be.
- Some of the ablation studies are missing. For example, the authors do not provide which layer of MDM ComMDM is placed in.
- The user study is not well explained. For example, how the users were asked to rate the models is not clear.

### Suggestions

The paper would benefit from a more thorough ablation study, particularly regarding the placement of the ComMDM layer within the MDM architecture. While the authors mention using the last layer, a more detailed analysis exploring the impact of different layer placements on performance would be valuable. This should include quantitative metrics, such as FID scores, for each configuration. For instance, the authors could experiment with placing ComMDM in earlier layers and report the resulting changes in motion quality and diversity. This would provide a more complete understanding of the model's sensitivity to architectural choices and help justify the final design. Furthermore, it would be beneficial to explore the impact of the number of layers used in the ComMDM block itself, as this could also affect the model's ability to capture complex motion patterns. 

The user study section needs significant improvement to ensure the validity and reliability of the results. The current description lacks crucial details about the experimental setup and the specific instructions given to the participants. It is essential to clarify how the text descriptions were used in the user study. Were the participants shown the text descriptions before rating the motion quality, or were the text descriptions used as part of the task description? If the participants were asked to evaluate the quality of the text-to-motion mapping, then it is important to include a baseline method that is designed for text-to-motion tasks. The current comparison with MRT, which is designed for motion completion, is not appropriate for this task. A more suitable baseline, such as a state-of-the-art text-to-motion model, should be included to provide a fair comparison. Additionally, the authors should provide more details about the participants, such as their background and experience with motion analysis, to ensure that the results are not biased by the participants' lack of expertise.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach. For example, the authors should discuss the potential challenges in generating long and complex motion sequences, as well as the limitations of the model in handling interactions between multiple people. It would also be beneficial to discuss the computational cost of the proposed approach and compare it to other methods. This would provide a more balanced view of the strengths and weaknesses of the proposed approach and help guide future research in this area. The authors should also consider including a qualitative analysis of the generated motions, highlighting the types of motions that the model can generate effectively and the types of motions that it struggles with. This would provide a more nuanced understanding of the model's capabilities and limitations.

### Questions

1. In Table 1, some of the R-precision numbers are bold that should not be.
2. In Table 2, why are some numbers bold and some are underlined?
3. In Table 3, why is the L2 error for ComMDM bold and not the lowest?
4. Can the authors explain the user study in more detail? For example, how the users were asked to rate the models is not clear.
5. Can the authors explain why they compare MRT with ComMDM in the user study for the text-to-motion task? MRT is designed for the motion completion task and not text-to-motion. So, it is not clear why the authors compare these two models.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
