from PySide6.QtWidgets import QDialog
from ebf_domain.rules.validation_result import ValidationResult
from ebf_ui.binding.validation.validation_binding import ValidationBinding, bind_validation
from ebf_ui.state.state_tracker import StateTracker
from ebf_ui.widgets.fields.combo_box_binding import ComboBoxBinding
from ebf_ui.widgets.fields.line_edit_binding import LineEditBinding
from ebf_ui.widgets.forms.form_binding import FormBinding

from ebf_trading_ui.forms.option_entry.ui_trade_entry_form import Ui_tradeEntryDialog
from ebf_trading_ui.view_models.ports.trade_record import TradeRecord
from ebf_trading_ui.view_models.position_spec import ALL
from ebf_trading_ui.view_models.trade_entry_view_model import TradeEntryViewModel


class TradeEntryForm(QDialog):

    def __init__(self, record: TradeRecord, parent=None):
        super().__init__(parent)

        self.ui = Ui_tradeEntryDialog()
        self.ui.setupUi(self)

        self._build_model(record)
        self._build_validation()
        self._setup_bindings()
        self._setup_commands()

    # region Setup
    def _build_model(self, record: TradeRecord) -> None:
        self.model = TradeEntryViewModel.from_record(record)
        self.tracker = StateTracker(self.model)

    def _build_validation(self) -> None:
        self.validation = ValidationBinding(validate=self._validate)

    def _setup_bindings(self) -> None:
        bind_validation(self.tracker, self.validation)

        self.position_binding = ComboBoxBinding(
            combo_box=self.ui.position,
            tracker=self.tracker,
            items=ALL,
            get_text=str,
            get_value=lambda: self.model.position_spec,
            set_value=lambda value: setattr(self.model, "position_spec", value),
        )
        
        self.fill_time_binding = LineEditBinding(
            line_edit=self.ui.fillTime,
            tracker=self.tracker,
            get_value=lambda: self.model.fill_time,
            set_value=lambda value: setattr(self.model, "fill_time", value),
        )

        self.form = FormBinding([
            self.position_binding,
            self.fill_time_binding,
        ])

        self.tracker.begin_edit()

    # endregion

    # region Validation
    def _validate(self) -> ValidationResult:
        return self.model.validate()

    # endregion

    # region Commands
    def _setup_commands(self) -> None:
        self.ui.saveButtonBox.accepted.connect(self._save)
        self.ui.saveButtonBox.rejected.connect(self.reject)

    def _save(self) -> None:
        pass
    # endregion
