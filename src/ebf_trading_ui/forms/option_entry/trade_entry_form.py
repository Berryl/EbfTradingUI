from PySide6.QtWidgets import QDialog
from ebf_ui.binding.validation.validation_binding import ValidationBinding, bind_validation
from ebf_ui.state.state_tracker import StateTracker
from ebf_ui.widgets.fields.combo_box_binding import ComboBoxBinding
from ebf_ui.widgets.forms.form_binding import FormBinding

from ebf_trading_ui.forms.option_entry.ui_trade_entry_form import Ui_tradeEntryDialog
from ebf_trading_ui.view_models.position_spec import ALL, PositionSpec


class TradeEntryForm(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_tradeEntryDialog()
        self.ui.setupUi(self)

        self._build_model()
        self._build_validation()
        self._setup_bindings()

    # region Setup
    def _build_model(self) -> None:
        self.tracker = StateTracker()
        self.position_spec: PositionSpec | None = None

    def _build_validation(self) -> None:
        self.validation = ValidationBinding(validate=self._validate)

    def _setup_bindings(self) -> None:
        bind_validation(self.tracker, self.validation)

        self.position_binding = ComboBoxBinding(
            combo_box=self.ui.position,
            tracker=self.tracker,
            items=ALL,
            get_text=str,
            get_value=lambda: self.position_spec,
            set_value=lambda v: setattr(self, "position_spec", v),
        )

        self.form = FormBinding([
            self.position_binding,
        ])

        self.tracker.begin_edit()

    # endregion

    # region Validation
    def _validate(self):
        from ebf_domain.rules.validation_result import ValidationResult
        return ValidationResult.success()

    # endregion

    # region Commands
    def _save(self) -> None:
        pass
    # endregion
