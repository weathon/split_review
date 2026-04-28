# Articulate-Anything:  Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 6, 3, 6, 8

## Abstract
Interactive 3D simulated objects are crucial in AR/VR, animations, and robotics, driving immersive experiences and advanced automation. However, creating these articulated objects requires extensive human effort and expertise, limiting their broader applications. To overcome this challenge, we present \articulate, a system that automates the articulation of diverse, complex objects from many input modalities, including text, images, and videos. \articulate leverages vision-language models (VLMs) to generate code that can be compiled into an interactable digital twin for use in standard 3D simulators. Our system exploits existing 3D asset datasets via a mesh retrieval mechanism, along with an actor-critic system that iteratively proposes, evaluates, and refines solutions for articulating the objects, self-correcting errors to achieve a robust outcome. Qualitative evaluations demonstrate \textsc{Articulate-Anything}'s capability to articulate complex and even ambiguous object affordances by leveraging rich grounded inputs. In extensive quantitative experiments on the standard PartNet-Mobility dataset, \articulate substantially outperforms prior work, increasing the success rate from 8.7--12.2\% to 75\% and setting a new bar for state-of-the-art performance. We further showcase the utility of our system by generating 3D assets from in-the-wild video inputs, which are then used to train robotic policies for fine-grained manipulation tasks in simulation that go beyond basic pick and place. These policies are then transferred to a real robotic system.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method for generating simulated 3D objects, with moving parts, that can be inferred with from multi-modal inputs (text, images, videos). This is interesting because is suggests a method of inferring models of objects, so that (robot) agents can be trained on richer and more representative simulations for things that exist in the real world. 

The method leverages LLMs to generate URDF descriptions (effectively code) which can then be iteratively refined based on feedback from a critic module. This is a neat use of LLMs that follows a trend in ML, but is well applied here.

Success is primarily evaluated by taking ground-truth URDF descriptions from an existing dataset (PartNet-Mobility), masking out information in them, and then comparing the reconstructed URDF with the ground-truth, using a threshold tolerance to define "success rates".

### Strengths
This paper does a lot of interesting things. Most of all, the idea of using LLMs to generate code is well applied here, and carried through evaluations that lead to at least proof of concept robot applications (though I believe still in simulation).

To the best of my knowledge, this is an *original* and *significant* contribution. For example, I don't know the prior work well, but the baselines sound reasonable.

The *quality* and *clarity* of the paper is decent as well, though could be improved (I have some suggestions below).

The multi-modality of the approach is also notable, and I appreciated the ablation of the different modalities (section 5.1).

### Weaknesses
Three weaknesses in the paper stood out but could be improved in revision. 

The first is relatively minor, but there seemed to be missing references to other works that have used LLM agents in an actor-critic setup. 

One paper that came to mind was the Text2Reward paper (https://arxiv.org/abs/2309.11489v3). But more generally, it would help to emphasise that this general idea - which is very cleverly used here - is not part of the paper's novely.

The second weakness is a lack of statistics and confidence intervals in the results. 

For example, Table 1 shows average joint prediction errors and it is possible to see differences between these averages. But without statistical testing (e.g. F-test or t-tests) it is hard to appreciate how meaningful these differences are. Some measure of variance would be useful here too (e.g. +/- standard deviation, to appreciate the consistency of the different models). In general, plotting more than summary statistics (e.g. averages) would be much stronger (e.g. violin or raincloud plots).

Relatedly, the Figure 5 caption says that the approach "significantly outperforms all baselines". But as before, there are no statistical tests to back this up - just comparative %success rages without confidence intervals. I agree that the proposed model results appear better, but without a sense of the confidence intervals it's hard to be certain. In this case, Chi-square tests (if the samples are large) or Fisher's exact tests (for smaller sample sizes) might be appropriate.

The final weakness might be harder to address as it concerns fitting all of the main results into the main body of the paper. 

To me, it was most notable that the application for robotics section felt incomplete and even confusing. I was not able to properly evaluate what was done or whether it was good based on the short section, which is a shame because it is a very interesting culmination of what the paper builds to. The paper also frames this as a key result, but then doesn't quite get all the way there.

Of course I appreciate that there are page limits, and I see that there are additional details in an appendix. But it would be better to fit more of that into the main paper for completeness.

Similarly, the in the wild results seemed incomplete in the main text as well, though I see there are more details in the appendix.

### Questions
In addition to the questions implied above, could I also ask if you experimented with weighting the losses in Eq 1? 

In section 5, on page 6, you also write that "Success requires all criteria to be within a small threshold... The position threshold is set to 50mm and the angular threshold to 0.25 radian (∼ 14.3 degree)." 

How did you choose these thresholds? Some defence of or rationale for these choices would be helpful, unless they are arbitrary?

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
3

### Summary
*Articulate-Anything* is a system that automates the articulation of complex objects from various input types, including text, images, and videos. It utilizes vision-language models (VLMs) to generate code that creates interactable digital twins compatible with 3D simulators. The system incorporates a mesh retrieval mechanism to leverage existing 3D assets and employs an actor-critic approach to iteratively propose, assess, and refine articulations, self-correcting to enhance accuracy.

### Strengths
1. Compared to previous works, this approach can begin with various inputs, including text, images, and videos.

2. By using iterative refinement with an actor-critic model, this method generates articulated assets with greater accuracy than prior approaches.

3. It utilizes vision-language models (VLMs) to perform the task without requiring network training or fine-tuning, eliminating the need for large-scale datasets, which are challenging to obtain for articulated objects.

### Weaknesses
1. While VLMs hold the potential to go beyond existing dataset, this method retrieves parts from those datasets. Thus, it is still constrained by existing datasets.

2. The framework is mainly prompting VLMs to construct articulated objects, with limited technical contributions. And the iterative refinement phrase only raise limited accuracy.

### Questions
1. What types of inputs does this work use when comparing to prior methods? Are these inputs—such as text, images, or videos—consistent with those used in previous works?

2. In terms of object retrieval, since this work aims to create digital twins from real-world observations, does the generated articulated object accurately resemble the real-world counterpart? Given that retrieval relies on CLIP scores based on text descriptions, the generated objects might be different from the original objects.

3. Could accuracy be reported across different object categories? Performance might vary significantly by category; for instance, simpler objects like windows and storage furniture may be easier to generate, whereas complex items like toilet seats or shopping carts could present more challenges.

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
This paper proposes Articulate-Anything, a closed-loop vision-language actor-critic system that is capable of converting real objects (provided via image, video, or text descriptions) into Python codes and further compiles them into URDFs. The proposed approach is evaluted against baselines of previous proposes and noticable improvements over success rates of link placement and joint prediction are achieved.

### Strengths
1. The paper is well-motivated. Understanding the structure of articulated objects is important for vision and robotics tasks.
2. The idea of closed-loop iterative refinement is interesting and technically sound.
3. The approach is able to handle diverse input modalities, including texts, images, and videos.
4. It is a good idea to use structural representations like code to model articulation structures.

### Weaknesses
1. It is not explained how the retrived part meshes do not conflict with each other. For example, in Fig.4(a), the code fragments do not show mechanisms preventing the 'door' having collisions with the drawer in the 'furniture_body'. In other words, how is the detailed position of the 'door'  (including its height) determined?

2. Some technical details are not clear. For example, the target affordance extraction part in Sec.4.4 and how link placement / joint prediction works for text / visual inputs, as the mesh retrieval results of text / visual inputs are different. A pseudo code can be help.

3. It seems that the method and experiments do not support well the task studied in this paper. According to Sec.3, the task is consistent with a formulation of reconstruction task. However, the proposed approach reterives similar meshes from a dataset rather than reconstruct the mesh in Sec.4, which cannot ensure the consistency between the retrieved mesh and the real object part and may result in large L_mesh. And the experiments just quantitatively evalutate the accuracy of link placement and joint prediction. Evaluations with important metrics like CD for reconstruction are not provided.

4. The robotic application is not solid enough. The test results like the success rate of different manipulation tasks are not provided, making it difficult to give a proper evalulation on the effectiveness of the generated assets. And additional real-world experiments will make this point stronger.

### Questions
1. According to Fig.3, a template object is retrieved when visual input is provided. How do the follow-up link prediction and joint prediction steps work on template objects? I assume that the link and joint information of the template object are already provided in PartNet-Mobility dataset.

2. What are the 'dimensions' given by the Layout Planner based on? How to ensure that the dimensions of multiple object parts given by the Planner are not contradictory?

3. Using VLMs to directly output numerical values (dimensions, angles, etc.) seems not a good idea for embodied applications which have high demands on safety and reliability, as studies have shown that LLMs are not strong enough to process numerical operations.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a system designed to automate the articulation of complex 3D objects for applications in AR/VR, animations, and robotics, addressing the challenge of extensive human effort required in traditional methods. It utilizes vision-language models (VLMs) to convert inputs such as text, images, and videos into interactable digital twins for 3D simulators. The system incorporates a mesh retrieval mechanism from existing 3D datasets and actor-critic frameworks to iteratively refine object articulation, achieving robust results.

### Strengths
1. The proposed methods for automatically modeling articulated objects address an interesting and meaningful topic, with potential to greatly benefit fields such as robotics.

2. The techniques introduced are well-founded. By leveraging vision-language models (VLMs), which encode valuable information about object affordances, the system effectively determines common articulations for various objects.

3. The paper provides a detailed analysis of failure cases, as shown in Figure 8, highlighting how the proposed pipeline outperforms other methods and identifying areas for further improvement.

4. The paper is well-written and easy to follow, making the concepts accessible to readers.

### Weaknesses
1. The proposed methods have only been validated on limited types of articulated objects (i.e., prismatic and revolute). When the types become more complex, such as cylindrical or universal joints, the current pipeline may struggle to handle these cases. The lack of evaluation on more complex joint types limits the generalizability of the approach. For instance, objects with helical motion or combinations of rotational and translational degrees of freedom are not addressed, which are common in many real-world scenarios.

2. The pipeline has only been tested using Google's Gemini VLM. It is recommended to conduct ablation studies to assess whether the inference performance varies with different VLM architectures, in order to evaluate the system's robustness. The reliance on a single VLM model raises concerns about the system's dependence on that specific architecture and its potential biases. The performance could be significantly affected by the VLM's internal representations and training data, which are not explored in this work.

### Questions
1. Could the authors provide examples illustrating how the performance of link placement and joint prediction evolves over the iterations?

2. Does the number of prompted examples affect the pipeline's performance? It would be helpful if the authors could provide an ablation study on the number of prompted items to determine whether performance varies based on this factor.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes a retrieval method for generating articulated objects in a simulator, taking into account both link and joint placement. It also demonstrates promising results in partner mobility

### Strengths
The proposed method for generating digital twins of articulated objects is intriguing and highly effective, significantly enhancing performance during evaluation. The website is comprehensive, offering visualizations and related code.

### Weaknesses
Please refer to 'Questions' section

- Is there any failure case analysis? For example, under what circumstances does the retrieval process select the wrong mesh? It would be helpful to show when retrieval might fail and how challenging those cases are.

- Concerns regarding Section 4.2:
  1) For instance, in Fig. 4a (left example), 'furniture body'  is place to the left relative to the 'door'. Since the body has thickness, why is the door placed on the left side of the front surface rather than the back? As the description only defines 2D spatial relationships, it's unclear how to position the link in 3D space.
  2) How many candidates does the actor's output generate? Can the relation fully cover all possibilities?

- Regarding Section 6's robotic experiment, where do the generated assets come from? Does Articulated Anything input video or images from RoboSuite to generate assets, and then train PPO with the generated assets, instead of directly using the assets in RoboSuite?

### Questions
- Is there any failure case analysis? For example, under what circumstances does the retrieval process select the wrong mesh? It would be helpful to show when retrieval might fail and how challenging those cases are.

- Concerns regarding Section 4.2:
  1) For instance, in Fig. 4a (left example), 'furniture body'  is place to the left relative to the 'door'. Since the body has thickness, why is the door placed on the left side of the front surface rather than the back? As the description only defines 2D spatial relationships, it's unclear how to position the link in 3D space.
  2) How many candidates does the actor's output generate? Can the relation fully cover all possibilities?

- Regarding Section 6's robotic experiment, where do the generated assets come from? Does Articulated Anything input video or images from RoboSuite to generate assets, and then train PPO with the generated assets, instead of directly using the assets in RoboSuite?

### Soundness
4

### Presentation
3

### Contribution
4
