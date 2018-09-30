from click.testing import CliRunner

from apparel_cli.main import mli


def test_entrypoint():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(mli, [], catch_exceptions=False)
        out = result.output_bytes.decode('utf-8')
        assert "Usage: mli [OPTIONS] COMMAND [ARGS]" in out
        assert "Options:" in out
        assert "  --help  Show this message and exit." in out
        assert "Commands:" not in out
