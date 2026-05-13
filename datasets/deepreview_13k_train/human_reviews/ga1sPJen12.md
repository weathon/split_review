# Craftium: Creating Efficient Environments for Open-Ended and Embodied Agents Beyond Gridworlds

- Decision: Reject
- Scores: 8, 3, 8, 6

## Abstract
Advancements in open-ended and embodied AI require highly adaptable and computationally efficient environments. Yet, existing platforms often lack the flexibility, efficiency, or richness necessary to drive progress in these areas. Research in fields related to open-endedness, such as unsupervised environment design and continual reinforcement learning, usually defaults to simplistic 2D grid environments, as more complex alternatives are either too rigid or computationally expensive. Conversely, in embodied AI, the field relies on fully featured video games like Minecraft, which are rich in content but computationally inefficient and offer limited customization for creating new tasks. This paper introduces Craftium, a framework based on the open-source Minetest game engine, providing a highly customizable, easy-to-use, and efficient platform for building rich Minecraft-like 3D environments. We showcase environments of different complexity and nature: from simple reinforcement learning tasks to a vast world with many creatures and biomes, along with a customizable procedural task generator. Conducted benchmarks show that Craftium substantially improves the computational cost of Minecraft-based frameworks, achieving +2K steps per second more.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Craftium, a new platform leveraging the open-source Minetest game engine to enable the creation of customizable, efficient, and rich 3D environments for research in RL and open-ended agent scenarios. Craftium is designed to bridge the gap between more simple 2D environments and computationally demanding, closed-source 3D platforms like Minecraft. Through various benchmark tests, the authors demonstrate that Craftium achieves significant performance gains, being notable faster than the Minecraft-based frameworks, and present use cases illustrating its flexibility for diverse RL tasks, procedural environment generation, and complex open-world simulations.

Minor comments:
- There is a typo on line 1027 “Then, the agent that the agent, …” 
- This paper seems like relevant work: Grbic, Djordje, et al. "Evocraft: A new challenge for open-endedness." Applications of Evolutionary Computation: 24th International Conference, EvoApplications 2021.

### Strengths
- Craftium addresses a critical limitation in AI research, especially in RL and embodied AI, by enabling complex and computationally feasible 3D environments that are both customizable and efficient.

- The paper presents comprehensive benchmark comparisons, e.g. MineDojo and VizDoom, demonstrating its advantage over current platforms in terms of computational performance and versatility.

- The authors provide clear explanations of Craftium’s architecture, including how Minetest’s open-source flexibility allows for modifications crucial for RL, such as reward functions and synchronous client-server interactions.

### Weaknesses
The framework currently supports single-agent settings, with multi-agent scenarios identified as future work. Given the growing interest in multi-agent RL, this limitation restricts Craftium’s immediate applicability for research in cooperative and competitive agent settings.

While the paper makes a valuable contribution to the field of environment design for embodied and open-ended AI research, the framework is basically "just" a wrapper around Minetest, thus limiting its novelty.

### Questions
Does the current framework support Minecraft Redstone components? These would be useful to allow agents to build more complex structures.

### Soundness
4

### Presentation
3

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
The paper presents Craftium, a framework designed to provide computationally efficient and customizable 3D environments for open-ended and embodied AI research, using the Minetest engine. Craftium aims to address limitations in existing environments, which are either computationally demanding or lack flexibility. The authors highlight its compatibility with the Gymnasium API, ease of use in procedural generation, and increased performance over other platforms like Minecraft.

### Strengths
- Craftium provides a complex 3D environment similar to Minecraft but offers faster performance, achieving over 2,000 steps per second compared to Minecraft-based frameworks.
- It allows for efficient procedural generation and supports a variety of reinforcement learning (RL) tasks.

### Weaknesses
 - The paper lacks a detailed comparison with other widely used simulators in robotics, such as IsaacGym, PyBullet, or MuJoCo, which also support 3D environments and open-world scenarios. Specifically, the paper should include comparisons with embodied simulators often used for high-level cognitive tasks, such as Habitat, AI2-THOR, and ProcTHOR. The current discussion does not adequately address the capabilities of these other simulators in the context of the paper's goals.
- The experimental comparisons are weak, and details on baseline and alternative environment performance are limited. The paper doesn’t clearly outline the real-world application of its contributions or benchmarks for similar environment capabilities in existing platforms. The environments shown in Figure 12 appear to be primarily 3D representations of 2D environments, and there is a lack of evidence showing the generation of genuinely rich and complex 3D environments.
- Overall, the novelty of the framework is minimal, as the setup resembles that of existing environments, with modifications focused on efficiency rather than new functionality. The paper does not sufficiently demonstrate the versatility and ease of use of the Lua API for designing rich 3D environments.
- In the procedural environment generation section, experiments demonstrated the generation of environments. However, all the generated environments can be represented using ASCII, meaning they are 2D environments. What is shown is a 3D representation of a 2D environment.
- In table 1, it is difficult to evaluate exactly if a framework is active or not after some time. There is no guarantee that this framework will still be active after a few months. Hence, I think that it is not a comparable characteristic.
- Missing related works that show the possibility of creating 3D environments in an open-ended way [1, 2, 3].

### Questions
- How does Craftium's procedural generation approach compare in diversity and scalability to existing frameworks in continuous and open-ended RL settings?
- Why is “spiders attack” a challenging task? It seems to have denser reward signals than “chop tree”.
- How do training of the tasks compare with that of existing simulators (e.g., MineDojo)? What is the performance against real time?
- In Figure 11, why are there 2 maximum red lines for the LLava-Agent? Why is it in % of steps, and not absolute number of steps?
- In Figure 12, why did the agent not manage to get any reward in the first 2 generated environments? They look like the simplest environments. In any of the generated environments, did the agent successfully complete the task of reaching the diamond?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Craftium, a framework for creating rich 3D environments for embodied and open-ended AI research. Key contributions:
- A flexible, efficient platform built on the open-source Minetest game engine
- Easy environment creation using Lua API instead of domain-specific languages
- Significant performance improvements over Minecraft-based frameworks (+2K steps/sec)
- Integration with the Gymnasium interface for compatibility with existing RL tools
- Comprehensive examples across different use cases (classic RL, open-ended learning, continual learning)

### Strengths
- Built on efficient C++ codebase (Minetest) versus Java (Minecraft)
- Strong compatibility through Gymnasium interface
- Addresses real needs in embodied/open-ended AI research
- Comprehensive benchmarks against VizDoom and MineDojo
- Diverse example environments demonstrating flexibility

### Weaknesses
 - Currently only supports single-agent scenarios
- Could use more ablation studies on design choices

The paper's claim that "Research in fields related to open-endedness... usually defaults to simplistic 2D grid environments" needs revision, as it overlooks significant recent developments in the field.

The emergence of foundation models has enabled several works to generate rich environments, such as OMNI-EPIC and EnvGen which use large language models for environment generation, but also environments such as Craftax which provides a sophisticated benchmark.

These works demonstrate that the field has already begun moving beyond simple grid-world environments. The authors should acknowledge this recent progress and better position their work within the context of these advances in environment generation for open-ended learning.

### Questions
- What are the key limitations in extending to multi-agent scenarios? Do you foresee potential challenges in extending Craftium to multi-agent scenarios, such as synchronization issues, increased computational requirements, or modifications needed to the Minetest engine.
- How does computational performance scale with environment complexity?
- What influenced the choice of Lua for environment creation?

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes `Craftium`, a framework based on MineTest. It is similar with MineCraft but open source and efficient.

### Strengths
1. The simulation is efficient.
2. The writing is good and experiments is detailed.
3. This framework is easy to use.

### Weaknesses
1. The difference between `Craftium` and Minecraft is not highlighted in figure 2 and I think it is important. What parts of figure 2 are not supported in MineCraft? 
2. The motivation of experiments are not clear.  In 3.5.2, the line 418 said 
> This example demonstrates how
Craftium environments can be used to analyze and evaluate the ability of large multimodal model based agents to leverage world knowledge to approach complex open-world tasks.

Is MineCraft also able to do this thing? If it is, I don't think it is your contribution. What's the meaning of rightmost icons of Figure 11?

3. In table 1, one of the advantage of `Craftium`  is "GYMNASIUM".  Can you give a detailed analysis of how GYMNASIUM implementation helps RL training?

4. There is no detailed or systematic analysis or examples on advantages of `Craftium` over MineCraft for RL. During RL, what information can `Craftium` give for a better learning but MineCraft cannot? I think detailed internal state/information should be the advantage.

### Questions
- See "Weakness".
- What's the motivation of compare LLava-Agent and PPO+LSTM in Sec 3.5.2?
- Can MineCraft support RL or environment generation? 
- I don't understand what's the disadvantages of MineCraft except the efficiency after reading. Can you compare the provided APIs between MineCraft and `Craftium`?

### Soundness
3

### Presentation
3

### Contribution
2
