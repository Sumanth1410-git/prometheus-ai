def test_python_environment_is_available():
    """Verify the Phase 0 Python test infrastructure is operational."""
    import sys

    assert sys.version_info >= (3, 13)
