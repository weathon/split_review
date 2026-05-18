- Decision: Accept
- Scores: 8, 8, 8, 6

## Merged Review

### Summary
This paper presents CLoSD, a closed-loop framework that combines a diffusion-based planner (DiP) with a reinforcement learning tracking controller (based on a simplified PHC) for text-driven multi-task character control. DiP is an autoregressive diffusion model conditioned on text prompts and target locations; the tracking controller executes the generated motion plans in physics simulation. The system is demonstrated on tasks including goal-reaching, object striking (hand/foot), sitting, and getting up.

### Strengths
- The paper is well-written, with clear contributions and relevant literature identified. Low-level technical details aid reproducibility.
- The goal of combining a motion diffusion model (MDM-type) with a physics-based controller (PHC) is clearly motivated, and the closed-loop integration is a simple yet interesting approach.
- CLoSD significantly outperforms prior methods (open-loop diffusion, text-to-motion RL systems, InterPhys, UniHSI) on multi-task benchmarks, especially for tasks requiring environmental interaction. High task success rates are reported.
- Extensive ablations demonstrate the effectiveness of design choices and hyper-parameter influence.
- The system enables on-the-fly text changes and multi-task execution with a single controller, reducing the need for task-specific fine-tuning.
- Code will be publicly available.

### Weaknesses
- **Limited experimental scope and clarity**: The experimental section lacks precision and could be better designed. Only four tasks are evaluated (goal-reaching, object striking, sitting, getting up); more diverse interactions are needed to demonstrate robustness and generalizability. One reviewer (Score 6) found the evaluation limited in scope compared to the claimed versatility.
- **Motion quality concerns**: The video exhibits noticeable shakiness, artifacts, and motions that appear to exploit physics (e.g., fast vibrations at 02:42). SMPL mesh renders show strong artifacts in hands and feet, less severe in MDM. The waving goodbye example is less accurate than MDM, raising a question whether CLoSD is overfitted to the specific tasks and limits diversity.
- **Contextualization and novelty**: The combination of a diffusion planner (CAMDM-type) with a tracker (PHC) is similar to prior hierarchical architectures (Trace and Pace, InsActor). The paper lacks depth in discussing how CLoSD advances beyond these works (e.g., motion in-painting, goal-reaching, chaining in InsActor). The main distinguishing feature is real-time generation, which largely comes from CAMDM; clearer exposition of unique contributions beyond that is needed (minority Review 4, Score 6).
- **Comparison issues**: 
  - *UniHSI*: The comparison omits the LLM planner; only a fixed pelvis target is used. The discrepancy between UniHSI’s original results (better quality, more complex chains like sitting on different objects, lying down) and the lower-quality outcomes here needs clearer explanation. Can CLoSD sit on variable heights? Where are its versatility limits?
  - *PhysDiff*: It would be more intuitive to compare directly with PhysDiff (MDM+physical projection) to isolate the benefit of the closed-loop approach. Why does CLoSD still have a high floating error of ~2 cm on average despite being physics-simulated?
  - *DiP vs. CAMDM*: A direct comparison between DiP and the Chen et al. 2024 architecture (CAMDM) is needed to justify why DiP is better suited.
  - *Controllers*: The paper uses a simplified PHC without mixture of experts. Questions: is this a single primitive policy trained with AMP and tracking rewards? How would full PHC compare? Would a controller that incorporates future frames (e.g., Chentanez et al. 2018) be more effective? Newer tracking controllers (2024) could be referenced. Controllers without reference motion could be discussed for feasibility of DiP integration.
- **Open-loop vs. closed-loop justification**: In Table 1, the open-loop setting performs well on goal reaching and object striking but struggles with sitting and getting up. Why is re-planning necessary for those tasks? The paper should elaborate on conditions where replanning is critical.
- **Prefix design risk**: Defining \(x^{\text{prefix}}\) as “current frames” risks the model forgetting previous plans. Could defining it as motion tracking errors or another design work better?
- **Engineering tricks and overfitting**: The method relies on many tricks (e.g., specifying joint target location and prompt to hit an object), making it unclear how much is due to human engineering vs. inherent capability. The approach appears overfitted to the demonstrated set of motions/tasks, not fully leveraging the generative capacity of the diffusion model.
- **Missing discussion of limitations**: Limitations are not clearly stated. MDM and PHC individually support diverse motions, but CLoSD’s presented motions are more constrained.
- **Future directions**: Can sensory inputs (e.g., vision) be incorporated for more complex environments? What are potential failure modes for longer planning horizons or more intricate sequences? (Reviewer 1 questions)