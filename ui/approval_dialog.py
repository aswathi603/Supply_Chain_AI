"""
Human Approval Dialog

Displays a confirmation dialog for high-impact
actions before execution.
"""

import streamlit as st


def approval_dialog(
    action_description: str,
) -> bool:
    """
    Render an approval dialog.

    Returns
    -------
    bool
        True if approved.
        False otherwise.
    """

    st.warning("⚠️ Human Approval Required")

    st.markdown(

        f"""
A high-impact operation has been requested.

**Action**

> {action_description}

Please review the action before continuing.
""",

    )

    approve_col, reject_col = st.columns(2)

    with approve_col:

        approve = st.button(

            "✅ Approve",

            use_container_width=True,

            type="primary",

        )

    with reject_col:

        reject = st.button(

            "❌ Reject",

            use_container_width=True,

        )

    if approve:

        st.success(

            "Action approved."

        )

        return True

    if reject:

        st.error(

            "Action rejected."

        )

        return False

    return False