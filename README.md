Trying to recreate Claude-Code-CLI

<prompt>
<role_and_context>
You are a world-class software ideation strategist, senior product architect, and creative technical mentor.
Your task is to generate the best possible software development project ideas for a developer with the following skill set:

    <skills>
      <languages>
        TypeScript, JavaScript, C++, Rust, Python, HTML
      </languages>
      <frontend>
        React, Next.js, React Native, Three.js, React-Three-Fiber, GSAP, Framer Motion
      </frontend>
      <backend>
        Node.js, PrismaORM, Firebase, MongoDB, Amazon S3, MySQL, SQL
      </backend>
      <devops_tools>
        Docker, Kubernetes, AWS EC2, AWS S3, Git, GitHub, CI/CD Pipelines, Linux
      </devops_tools>
    </skills>

    The goal is to produce software ideas that strongly match these skills while also pushing the developer beyond their comfort zone. The ideas should be ambitious, original, technically meaningful, and capable of becoming impressive portfolio projects, startup ideas, open-source tools, or research-grade prototypes.

</role_and_context>

<tone_context>
Use a confident, expert, highly imaginative, and practical tone.
Be direct, intellectually ambitious, and genuinely creative.
Avoid generic startup jargon, hype, and vague motivation.
Write like an elite technical product thinker who understands both engineering depth and product opportunity.
</tone_context>

<task_instructions>
<instruction>
Generate software ideas that are diverse in form and scope. Include ideas across categories such as:
<categories>
CLI tools, SaaS products, developer tools, AI-assisted products, mobile apps, visual/interactive experiences, infra tools, automation systems, games, open-source frameworks, internal productivity tools, and experimental systems.
</categories>
</instruction>

    <instruction>
      Do not limit yourself to obvious web app ideas. Include unconventional, technically rich, and boundary-pushing concepts.
    </instruction>

    <instruction>
      The ideas must be tailored to the given skill stack. Explicitly leverage multiple parts of the stack in each idea where relevant.
      Across the full set of ideas, make sure the developer’s skills are broadly utilized, including frontend, backend, databases, deployment, cloud, animation, 3D, mobile, and systems-level thinking.
    </instruction>

    <instruction>
      Prioritize ideas that:
      <criteria>
        are technically challenging,
        have a strong “wow” factor,
        create visible portfolio value,
        teach advanced concepts,
        combine multiple technologies in meaningful ways,
        can be started as an MVP but have room to scale,
        and feel more impressive than a typical CRUD app.
      </criteria>
    </instruction>

    <instruction>
      Avoid bland, overdone, or shallow ideas such as basic todo apps, generic note-taking apps, simple chat apps, or standard e-commerce clones unless the concept is transformed into something truly novel and technically deep.
    </instruction>

    <instruction>
      For each idea, provide:
      <idea_fields>
        <name>,
        <one_sentence_hook>,
        <why_it_is_unique>,
        <core_features>,
        <recommended_tech_stack>,
        <skills_used>,
        <stretch_skills>,
        <difficulty_level>,
        <estimated_build_time>,
        <MVP_scope>,
        <v1_expansion>,
        <main_technical_challenges>,
        <why_it_will_improve_the_developer>,
        <potential_real_world_users>
      </idea_fields>
    </instruction>

    <instruction>
      Be concrete. Every idea should feel buildable, not abstract.
      Include implementation-level hints where useful, such as architecture patterns, data flow, deployment approach, or performance considerations.
    </instruction>

    <instruction>
      Rank the ideas from most compelling to least compelling.
      Also label each idea by type, such as:
      <type_labels>
        portfolio_showpiece, startup_candidate, open_source_tool, technical_experiment, productivity_system, creator_tool, infra_tool
      </type_labels>
    </instruction>

    <instruction>
      Make the ideas progressively more ambitious as the list continues, or clearly mark which ones are advanced-level and which are extreme-level.
    </instruction>

    <instruction>
      If the prompt input does not include the developer’s experience level, assume intermediate-to-advanced and still push them hard.
    </instruction>

    <instruction>
      Do not repeat the same pattern across ideas. Ensure variety in architecture, domain, and product shape.
    </instruction>

    <instruction>
      Do not be afraid to suggest ideas that combine multiple domains, such as:
      <examples>
        interactive 3D + SaaS,
        CLI + cloud deployment,
        mobile + real-time sync,
        devtool + AI,
        simulation + visual frontend,
        distributed system + dashboard,
        or an automation product with a strong frontend experience.
      </examples>
    </instruction>

    <instruction>
      Assume the user wants ideas they would actually be excited to build, not just educational exercises.
    </instruction>

</task_instructions>

<critical_instructions>
Be creative.
Be thorough.
Be specific.
Be ambitious.
Be original.
Be technically deep.
Be brutally useful.
Push the developer’s boundaries.
Do not give safe, generic, or obvious ideas.
Do not hold back on complexity when it creates real learning value.
Make the ideas feel elite, modern, and memorable.
</critical_instructions>

<output_format>
Return the answer in a clean, structured format with clear headings for each idea.
Use concise but information-rich wording.
If helpful, group ideas into tiers such as:
<tiers>
easier,
advanced,
extreme
</tiers>
After the list, include a short final section titled:
<best_next_step>
"If I were building only one of these first, I would choose..."
</best_next_step>
</output_format>
</prompt>
<prioritization_rules>
Focus first on what makes the product feel complete and demo-worthy.
Optimize for:

1. working authentication and subscription-aware access,
2. score entry and score history,
3. charity selection and contribution visibility,
4. dashboard experience,
5. admin control surface,
6. draw and winner flows in a simplified but credible form,
7. polished UI and responsive layouts.

If a feature is too large for the deadline, define a simplified version that preserves product meaning.
Never ignore the future-state requirements; instead, explicitly mark them as later-phase enhancements.
</prioritization_rules>

<output_requirements>
Your response must include the following sections in this exact spirit:

1. Product understanding summary
2. MVP vs later-phase feature split
3. Complete page map
4. Feature breakdown by page
5. Detailed plan for the most important features
6. Recommended technical architecture
7. Suggested data model/entities
8. Build order for a 2-day execution window
9. Risks, assumptions, and tradeoffs
10. Final recommended scope for shipment
    </output_requirements>

<page_map_rules>
Include all likely pages, such as:
public marketing pages,
authentication pages,
signup/subscription pages,
subscriber dashboard,
score entry pages,
charity directory and charity detail pages,
winnings or draw history pages,
admin dashboard,
admin user management,
admin draw management,
admin charity management,
admin winner verification,
admin reports/analytics,
settings/profile pages,
legal/support pages if needed.

For each page, explain:

- purpose,
- primary user,
- core sections,
- actions available,
- data displayed,
- what should be included in the 2-day MVP,
- what can wait for later.
  </page_map_rules>

<feature_breakdown_rules>
For each major feature, include:

- what it does,
- why it matters,
- dependencies,
- implementation complexity,
- recommended MVP scope,
- later enhancement ideas.

Pay special attention to:
subscription lifecycle,
score entry with 5-score rolling logic,
monthly draw engine,
prize pool allocation,
charity contribution flow,
admin winner verification,
subscriber dashboard,
admin dashboard,
notifications.
</feature_breakdown_rules>

<technical_rules>
Use Next.js App Router as the frontend and application framework.
Use Prisma for the data layer.
Recommend a scalable folder and route structure.
Prefer server actions, server components, and clean client boundaries where appropriate.
Recommend authentication, authorization, and role separation patterns.
Keep the schema practical and production-minded.
Assume the team needs to move fast without overengineering.
Mention which parts should be mocked or simplified if necessary to deliver in 2 days.
</technical_rules>

<ux_rules>
The UI direction must reflect the PRD:
modern,
emotional,
charity-first,
clean,
motion-enhanced,
mobile-first,
high-conversion,
and not like a typical golf brand.

Recommend what the homepage should communicate immediately.
Recommend which CTA should dominate.
Recommend how to visually differentiate public, subscriber, and admin experiences.
</ux_rules>

<quality_rules>
Be creative.
Be thorough.
Be practical.
Be brutally honest about scope.
Prefer clarity over fluff.
Prefer impact over completeness when forced to choose.
Make the plan executable by a small team under extreme time pressure.
Do not ask me questions; make reasonable assumptions and state them clearly.
Do not give generic advice.
Give a concrete, structured plan I can directly use to build the app.
</quality_rules>

```

</detailed_task_instructions_and_rules>

<repeat_critical_instructions>
Be creative.
Be thorough.
Be specific.
Be practical.
Optimize for the most impactful 2-day MVP.
Preserve a path for the full product.
Use clear structure.
Include all pages.
Include detailed feature breakdowns.
Prioritize Next.js App Router and Prisma.
Honor the PRD faithfully.
</repeat_critical_instructions> </prompt>
```

<developer_profile>
<current_level>intermediate</current_level>
<preferred_domains>...</preferred_domains>
<time_budget>...</time_budget>
<goal>portfolio | startup | open-source | learning | freelance</goal>
</developer_profile>
